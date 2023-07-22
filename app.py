import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        response = openai.Completion.create(
            model="text-davinci-003",
            max_tokens = 150,
            prompt=generate_prompt(topic),
            temperature=0.6,
        )
        print("This is response ------------------------------")
        print(response)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    print("This is result ------------------------------")
    print(type(result))
    print(result)
    return render_template("index.html", result=result)


def generate_prompt(topic):
    return """Suggest three resouces to learn more about a topic.


topic: {}
resouces:""".format(
        topic.capitalize()
    )
