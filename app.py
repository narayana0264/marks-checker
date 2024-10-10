#</h1></body></html>"


from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'kjf iwqhfiqw qoifhqo'

@app.route('/success/<int:score>')
def success(score):
    return "passed -> marks is" + str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "failed -> marks is" + str(score)


@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

if __name__=='__main__':
    app.run(debug=True)