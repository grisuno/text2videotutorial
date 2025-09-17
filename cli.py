#!/usr/bin/env python3
# _*_ coding: utf8 _*_
"""
main.py

Autor: Gris Iscomeback
Correo electrónico: grisiscomeback[at]gmail[dot]com
Fecha de creación: 09/06/2024
Licencia: GPL v3

Descripción: Asistente de investigación por consola estilo GPT con Groq
"""
import re
import os
import argparse
import logging
import signal
import sys
import json
import time
from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from script_animator import generate_frames

BANNER = """
   _____           _       ___          _                 __             ___    ____
  / ___/__________(_)___  /   |  ____  (_)___ ___  ____ _/ /_____  _____/   |  /  _/
  \__ \/ ___/ ___/ / __ \/ /| | / __ \/ / __ `__ \/ __ `/ __/ __ \/ ___/ /| |  / /  
 ___/ / /__/ /  / / /_/ / ___ |/ / / / / / / / / / /_/ / /_/ /_/ / /  / ___ |_/ /   
/____/\___/_/  /_/ .___/_/  |_/_/ /_/_/_/ /_/ /_/\__,_/\__/\____/_/  /_/  |_/___/   
                /_/                                                                 
[*] Iniciando: LazyOwn Text to Video Script Assistant [;,;]
"""

HELP_MESSAGE = """
{message}

[?] Uso: python main.py --prompt "<tu prompt>" [--debug]

[?] Opciones:
  --prompt    "El prompt para la tarea de programación (requerido)."
  --debug, -d "Habilita el modo debug para mostrar mensajes de depuración."
  --transform "Transforma la base de conocimientos original en una base mejorada usando Groq."

[?] Asegúrate de configurar tu API key antes de ejecutar el script:
  export GROQ_API_KEY=<tu_api_key>
[->] visit: https://console.groq.com/docs/quickstart not sponsored link
"""

KNOWLEDGE_BASE_FILE = "knowledge_base.json"
IMPROVED_KNOWLEDGE_BASE_FILE = "knowledge_base_improved.json"
SCRIPTS_FOLDER = "scripts"

def signal_handler(sig: int, frame: any) -> None:
    print(f'\n[*] Interrupción recibida, saliendo del programa.')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def show_help(message: str) -> None:
    print(HELP_MESSAGE.format(message=message))
    sys.exit(1)

def check_api_key() -> str:
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        api_key = 'gsk_01234567899876543210'
       
    return api_key


def configure_logging(debug: bool) -> None:
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='[+] LazyGroqPT Asistente de Tareas de Programación.')
    parser.add_argument('--prompt', type=str, required=True, help='El prompt para la tarea de programación/Tarea Cli')
    parser.add_argument('--debug', '-d', action='store_true', help='Habilita el modo debug para mostrar mensajes de depuración')
    parser.add_argument('--transform', action='store_true', help='Transforma la base de conocimientos original en una base mejorada usando Groq')
    return parser.parse_args()

def create_complex_prompt(base_prompt: str, history: str, knowledge_base: str, error_message: str = None) -> str:
    error_context = f"El siguiente error ocurrió durante la ejecución: {error_message}" if error_message else "No se detectaron errores en la última iteración."
    return f"""
Eres un experto en crear scripts altamente profesionales y optimizados para uso en producción. Tu tarea es generar un script en Python que cumpla con los siguientes criterios:

El script debe incluir todas las bibliotecas necesarias para un rendimiento óptimo y uso en producción.
El código debe estar bien estructurado, ser eficiente y seguir las mejores prácticas.
El script está destinado a un tutorial, por lo que todas las explicaciones deben incluirse como comentarios en español.
Si no estás seguro sobre algún aspecto de los requisitos, haz entre 3 a 7 preguntas aclaratorias para entender completamente el objetivo antes de proceder.
Recuerda:

Solo responde con el script.
Todas las explicaciones deben estar escritas como comentarios en español.

El script es: 
{base_prompt}

Base de conocimientos:
{knowledge_base}

Mensajes anteriores:
{history}

{error_context}
"""

def load_knowledge_base(file_path: str) -> dict:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_knowledge_base(knowledge_base: dict, file_path: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(knowledge_base, f, indent=4)

def add_to_knowledge_base(prompt: str, command: str, file_path: str) -> None:
    knowledge_base = load_knowledge_base(file_path)
    knowledge_base[prompt] = command
    save_knowledge_base(knowledge_base, file_path)

def get_relevant_knowledge(prompt: str) -> str:
    knowledge_base = load_knowledge_base(KNOWLEDGE_BASE_FILE)
    relevant_knowledge = []
    for key, value in knowledge_base.items():
        if prompt in key:
            relevant_knowledge.append(f"{key}: {value}")
    return "\n".join(relevant_knowledge) if relevant_knowledge else "No se encontró conocimiento relevante."

def transform_knowledge_base(client) -> None:
    original_knowledge_base = load_knowledge_base(KNOWLEDGE_BASE_FILE)
    improved_knowledge_base = {}

    for prompt, command in original_knowledge_base.items():
        history = []
        error_message = None
        complex_prompt = create_complex_prompt(prompt, '\n'.join(history), '', error_message)
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": complex_prompt}],
                model="llama3-8b-8192",
            )
            improved_command = chat_completion.choices[0].message.content.strip()
            improved_knowledge_base[prompt] = improved_command
            time.sleep(2)
        except Exception as e:
            logging.error(f"[E] Error al comunicarse con la API: {e}")
            improved_knowledge_base[prompt] = command

    save_knowledge_base(improved_knowledge_base, IMPROVED_KNOWLEDGE_BASE_FILE)
    print(f"[+] Nueva base de conocimientos guardada en {IMPROVED_KNOWLEDGE_BASE_FILE}")

def save_script(script: str, script_name: str) -> str:
    if not os.path.exists(SCRIPTS_FOLDER):
        os.makedirs(SCRIPTS_FOLDER)
    script_path = os.path.join(SCRIPTS_FOLDER, script_name)
    with open(script_path, 'w', encoding='utf-8') as script_file:
        script_file.write(script)
    return script_path

def generate_video_from_script(script_path: str) -> None:
    bg_image_path = "image1.png"
    font_path = "typewriter.ttf"
    output_resolution = (640, 480)
    fps = 25
    char_per_sec = 10
    margins = 40
    output_path = "output_video.avi"
    audio_path = "background1.mp3"
    
    with open(script_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    generate_frames(text, bg_image_path, font_path, output_resolution, fps, char_per_sec, margins, output_path, audio_path)

def main() -> None:
    print(BANNER)
    
    args = parse_args()
    configure_logging(args.debug)

    api_key = check_api_key()
    model = 'llama3-8b-8192'
    groq_chat = ChatGroq(
        groq_api_key=api_key, 
        model_name=model
    )

    if args.transform:
        transform_knowledge_base(groq_chat)
        return

    base_prompt = args.prompt
    history = []
    error_message = None

    system_prompt = 'Eres un experto asistente de programación'
    conversational_memory_length = 5

    memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

    while True:
        relevant_knowledge = get_relevant_knowledge(base_prompt)
        complex_prompt = create_complex_prompt(base_prompt, '\n'.join(history), relevant_knowledge, error_message)
        error_message = None
        system_prompt_complex = f"{complex_prompt} {system_prompt}"
        try:
            prompt = ChatPromptTemplate.from_messages(
                [
                    SystemMessage(content=system_prompt_complex),
                    MessagesPlaceholder(variable_name="chat_history"),
                    HumanMessagePromptTemplate.from_template("{human_input}"),
                ]
            )

            conversation = LLMChain(
                llm=groq_chat,
                prompt=prompt,
                verbose=args.debug,
                memory=memory,
            )

            response = conversation.predict(human_input=base_prompt)
            code_content = re.search(r'```(.*?)```', response, re.DOTALL).group(1).strip()

            print(f"[R] Respuesta del modelo:\n{code_content}")

            script_name = f"script_{int(time.time())}.py"
            response = code_content
            script_path = save_script(response, script_name)
            print(f"[+] Script guardado en: {script_path}")

            generate_video_from_script(script_path)
            print(f"[+] Video generado a partir del script guardado.")

            history.append(f"User: {base_prompt}")
            history.append(f"AI: {response}")
            add_to_knowledge_base(base_prompt, response, KNOWLEDGE_BASE_FILE)

            base_prompt = input("\n[>] Ingresa el siguiente prompt (o 'exit' para salir): ")
            if base_prompt.lower() == 'exit':
                break

        except Exception as e:
            logging.error(f"[E] Error al comunicarse con la API: {e}")
            error_message = str(e)

if __name__ == "__main__":
    main()
