#!/usr/bin/env python3

from elevenlabs import voices, generate
from elevenlabs import set_api_key
set_api_key("xxxxxxxxxxxxxxxxxxxxxxxxxxx")
import os
from elevenlabs import save
import subprocess
from flask import Flask, jsonify, request, send_file
app = Flask(__name__)

@app.route('/tts', methods=['POST'])

def tts():
       data = request.get_json()
       text = data['text']
       print(text)

       audio = generate(
        text=text,
	voice="Bella",
        model="eleven_monolingual_v1"
       )
       tmp_path_opus=filename="/var/www/html/tts/output.opus"
       save(audio, tmp_path_opus)
       return send_file(tmp_path_opus, mimetype='audio/ogg, codecs=opus')


if __name__ == '__main__':
       app.run(host='localhost', port=9000)

