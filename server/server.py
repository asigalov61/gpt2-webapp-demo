from flask import Flask, escape, request
from flask_cors import CORS, cross_origin
import logging
import gpt2

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

logging.basicConfig(filename='input.log',level=logging.DEBUG)

@app.route('/')
def hello():
  return 'I am groot'

@app.route('/generate', methods=['POST'])
@cross_origin()
def generate():
  logging.info('INPUT_REQUEST: ' + request.json['text'])
  input = request.json['text']
  output = gpt2.generator(input)
  logging.info('OUTPUT_REQUEST: ' + output)
  return f'{input} {output}'

if __name__ == "__main__":
  app.run(host='0.0.0.0')