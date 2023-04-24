from app import *

def get_response_of_text(prompt):
    answer = openai.Completion.create(
    prompt=prompt,
    temperature=1,
    max_tokens=20,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    model=COMPLETIONS_MODEL)["choices"][0]["text"].strip(" \n")
    return answer