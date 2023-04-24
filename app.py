from flask import Flask, render_template, request
import openai
import os

COMPLETIONS_MODEL = "text-davinci-003"
openai.api_key = os.getenv('my_api_key')

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    
    if request.method == 'POST':
      prompt = request.form['prompt']
      answer = openai.Completion.create(
         prompt=prompt,
         temperature=1,
         max_tokens=500,
         top_p=1,
         frequency_penalty=0,
         presence_penalty=0,
         model=COMPLETIONS_MODEL)["choices"][0]["text"].strip(" \n")
      return answer
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
