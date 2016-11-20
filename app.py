# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import markovify
import random
import os

def is_int(input):
  try:
    num = int(input)
  except ValueError:
    return False
  return True

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=["GET", "OPTIONS"])
@cross_origin()
def index():

  size = ""

  if request.args.get('size') != None:
    size = unicode(request.args.get('size'))

  newSpeech = ""

  with open('source.txt') as f:
    rawText = f.read()

  model = markovify.Text(rawText, state_size=3)

  if size == "":
    for i in range(2):
      newSpeech += " " + model.make_sentence()
  elif size == "tweet":
    newSpeech += " " + model.make_short_sentence(140)
  elif is_int(size):
    for i in range(int(size)):
      newSpeech += " " + model.make_sentence()

  return jsonify({
    "content": newSpeech
  })

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
