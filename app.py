from flask import Flask, redirect, render_template, jsonify, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-key"

debug = DebugToolbarExtension(app)

# responses = []
finished = []

@app.route('/')
def index():
    return render_template('survey.html', 
    title=satisfaction_survey.title, 
    instructions=satisfaction_survey.instructions)

@app.route('/start_new_session', methods=["POST"])
def start_session(): 
    session["responses"] = []
    return redirect('/questions/0')

@app.route('/questions/<question_number>')
def questions(question_number):
    next_question = len(session["responses"])
    breakpoint()
    if finished:
        return redirect('/thankyou')
    elif next_question != int(question_number):
        flash("You're trying to access an invalid question!")
        return redirect(f'/questions/{next_question}')

    return render_template('question.html', 
    question=satisfaction_survey.questions[int(question_number)].question,
    choice=satisfaction_survey.questions[int(question_number)].choices
    )

@app.route('/answer', methods=["POST"])
def answers():
    session["responses"] = [*session["responses"], request.form['answer']]
    next_question = len(session["responses"])
    # breakpoint()
    if len(satisfaction_survey.questions) == next_question:
        return redirect('/thankyou')
    return redirect(f'/questions/{next_question}')

@app.route('/thankyou')
def thankyou():
    # Mutate original responses to be empty / don't create new responses variable
    finished.append(True)
    # responses.clear()
    session["responses"] = []
    return render_template('thankyou.html')