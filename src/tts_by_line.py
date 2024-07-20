from pathlib import Path
from openai import OpenAI
import os
import openai
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

# Open the text file and read lines
with open("robot-collisions/solution2.txt", "r") as file:
    lines = file.readlines()

# Path to save the MP3 files
base_path = Path(__file__).parent

# Loop through each line and create a separate MP3 file
for i, line in enumerate(lines):
    # Ensure non-empty lines are processed
    if line.strip():
        speech_file_path = base_path / f"robot-collisions/solution2/line_{i+1}.mp3"
        response = client.audio.speech.create(
            model="tts-1-hd", voice="alloy", input=line
        )
        response.stream_to_file(speech_file_path)
