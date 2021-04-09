from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('generate.html')

@app.route('/', methods=['POST'])
def my_form_post():
    start = request.form['start']
    end = request.form['end']

    number = random.randint(int(start), int(end))
    return render_template("generate.html", data=f"You got {str(number)}")

if __name__ == "__main__":
    app.run(debug=True)