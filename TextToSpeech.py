import os
from google.cloud import texttospeech
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'DrivelServiceAccount.json'
client = texttospeech_v1.TextToSpeechClient()

text = "hello world"

sythesis_input = texttospeech_v1.SynthesisText(text=text)

voice = texttospeech_v1