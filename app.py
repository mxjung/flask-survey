from flask import Flask, redirect, render_template, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-key"

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def index():
    return render_template('survey.html', 
    title=satisfaction_survey.title, 
    instructions=satisfaction_survey.instructions)


@app.route('/questions/<question_number>')
def questions(question_number):
    return render_template('question.html', 
    question=satisfaction_survey.questions[int(question_number)].question,
    choice=satisfaction_survey.questions[int(question_number)].choices
    )

@app.route('/answer', methods=["POST"])
def answers():
    responses.append(request.form['answer'])
    next_question = len(responses)
    breakpoint()
    return redirect(f'/questions/{next_question}')