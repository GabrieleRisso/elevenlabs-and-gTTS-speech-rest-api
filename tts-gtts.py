#!/usr/bin/env python3
import os
import subprocess
from flask import Flask, jsonify, request, send_file
app = Flask(__name__)

@app.route('/tts', methods=['POST'])

def tts():
       data = request.get_json()
       text = data['text']
       print(text)
       subprocess.run(['gtts-cli', '--lang=it', '-o', '/var/www/html/tts/output.mp3', text ])
       subprocess.run(['ffmpeg', '-i', '/var/www/html/tts/output.mp3', '-y', '-af', 'atempo=1.4,dialoguenhance,arnndn=m=/home/gabriele/progetti/whatsapp-chatgpt/filter.rnn,volume=1.3', '/var/www/html/tts/output.opus'])
       tmp_path_opus="/var/www/html/tts/output.opus"
       return send_file(tmp_path_opus, mimetype='audio/ogg, codecs=opus')


if __name__ == '__main__':
       app.run(host='localhost', port=8000)

