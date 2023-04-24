from flask import Flask, render_template, request
import openai
import os
import aiapi

COMPLETIONS_MODEL = "text-davinci-003"
openai.api_key = os.getenv('my_api_key')

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
  if request.method == 'POST':
    prompt = request.form['prompt']
    answer = aiapi.get_response_of_text(prompt)
    return answer

  return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run()
