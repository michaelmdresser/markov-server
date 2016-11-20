# -*- coding: utf-8 -*-

#  this generator has a default source of some chosen speeches of Obama's

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import markovify
import random
import os

# checks if input can be converted to an integer
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
  newSpeech = ""

  # size is used to determine the number of sentences to generate or if a tweet
  # should be generated
  if request.args.get('size') != None:
    size = unicode(request.args.get('size'))

  with open('source.txt') as f:
    rawText = f.read()

  model = markovify.Text(rawText, state_size=3)

  # generates a tweet, the chosen number of sentences, or defaults to two sentences
  if size == "tweet":
    newSpeech += " " + model.make_short_sentence(140)
  elif is_int(size):
    for i in range(int(size)):
      newSpeech += " " + model.make_sentence()
  else size == "":
    for i in range(2):
      newSpeech += " " + model.make_sentence()

  return jsonify({
    "content": newSpeech
  })

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
