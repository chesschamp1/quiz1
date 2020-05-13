
def get_totalscore(useranswer, useranswer2):
    totalscore = 0
    if useranswer == "Brazil":
        print("Yes! That's correct. Score: +1.")
        totalscore = totalscore+1
    else: 
        print("No, sorry the answer was Brazil.")
        totalscore = totalscore
    return totalscore



def get_question_1_results(useranswer):
    totalscore = 0
    message = ""
    if useranswer == "Brazil":
        message = "Yes! That's correct. Score: +1."
        totalscore = totalscore+1
    else: 
        message = "No, sorry the answer was Brazil."
        totalscore = totalscore
    return {
        "totalscore": totalscore,
        "message": message
    }

def get_question_2_results(useranswer2, totalscore):
    message = ""
    if useranswer2 == "China":
        message = "Yes! That's correct. Score: +1."
        totalscore = totalscore+1
    else: 
        message = "No, sorry the answer was China."
        totalscore = totalscore
    return {
        "totalscore": totalscore,
        "message": message
    }