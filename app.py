# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_totalscore, get_question_1_results, get_question_2_results

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == "POST":
        useranswer = request.form["useranswer"]
        question_1_results = get_question_1_results(useranswer)
        props = {
            "useranswer": useranswer,
            "message": question_1_results["message"],
            "totalscore": question_1_results["totalscore"]
        }
        return render_template("results_copy.html", props=props)
    else:
        return "error"

@app.route('/page3', methods=['GET', 'POST'])
def page3():
    if request.method == "POST":
        useranswer2 = request.form["useranswer2"]
        totalscore = int(request.form["totalscore"])
        question_2_results = get_question_2_results(useranswer2, totalscore)
        props = {
            "useranswer": useranswer2,
            "message": question_2_results["message"],
            "totalscore": question_2_results["totalscore"]
        }
        return render_template("page3.html", props=props)
    else:
        return "error"