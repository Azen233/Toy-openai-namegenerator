import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    Last_Name = ""
    if request.method == "POST":
        Last_Name = request.form["Last_Name"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = [{"role": "user", "content": generate_prompt(Last_Name)}],
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].message['content'],Last_Name = Last_Name))

    result = request.args.get("result")
    Last_Name = request.args.get("Last_Name")
    return render_template("index.html", result=result, Last_Namçe=Last_Name)


def generate_prompt(Last_Name):
    return """Suggest five first names for an last name.
Last_Name: {}
Names:""".format(
        Last_Name.capitalize()
    )
