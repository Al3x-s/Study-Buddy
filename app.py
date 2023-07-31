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
        print(f"This is response ------------------------------\n{response}")
        print(f"This is topic ------------------------------\n{type(topic)}")

    #if request.method == "POST" and len(request.form["curious"]) > 0:
     #   curious = requests.form["curious"]
      #  response2 = openai.Completion.create(
       #     model="text-davinci-003",
        #    max_tokens = 50,
         #   prompt = generate_qa(curious),
          #  temperature = 0.7
           #     )
        return redirect(url_for("index", result=response.choices[0].text, tokens_used=response.usage.completion_tokens))
    tokens_used = request.args.get("tokens_used")
    result = request.args.get("result")
    print(f"This is  args------------------------------{request.args}")
    print(f"this is result\n{result}")
    if str(type(result)) != "<class 'NoneType'>":
        result= result.split("---")
    return render_template("index.html", result=result, tokens_used=tokens_used)


def generate_prompt(topic):
    return """Suggest 5 resouces to learn more about a topic give one sentence explaining the resource right after the name of the resource format your answers so each answer is separated by '---' instead of commas.

topic:math
resources:Khan Academy "a free online learning platform with thousands of videos and exercises to help you learn math"--- Mathisfun "a website filled with interactive math activities and games"--- Mathantics "a website with video lessons and guided practice to help students understand math concepts"
topic: {}
resouces:""".format(
        topic.capitalize()
    )

#Redirect user to another page and present pt 2 of the page cuz this page is trash
# stop loop here this kills api calls
def generate_qa(question):
    return""" answer the following question to the best of your ability about the above topic""".format(question)
