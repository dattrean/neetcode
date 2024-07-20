import sys
from pathlib import Path
from openai import OpenAI
import os
import openai
from dotenv import load_dotenv

def main(folder_name):
    load_dotenv()
    openai.api_key = os.environ["OPENAI_API_KEY"]
    client = OpenAI()

    question_file_path = Path(__file__).parent / f"{folder_name}/question.txt"
    if not question_file_path.is_file():
        print(f"Error: {question_file_path} does not exist.")
        return

    with open(question_file_path, 'r') as file:
        text = file.read()

    speech_file_path = Path(__file__).parent / f"{folder_name}/question.mp3"
    response = client.audio.speech.create(
      model="tts-1-hd",
      voice="alloy",
      input=text
    )

    response.stream_to_file(speech_file_path)
    print(f"Speech file saved to {speech_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder-name>")
    else:
        folder_name = sys.argv[1]
        main(folder_name)
