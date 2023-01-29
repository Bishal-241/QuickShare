from flask import Flask,request, url_for, render_template as render , redirect

from api import dOprator
app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def main():
    if request.method == 'POST':
        messageString = request.form['message']
        print(messageString)
        return "Good your work is done!"
    else:
        return render('index.html')
    # return  render('index.html')



if(__name__ == "__main__"):
    app.run(debug=True, port=5000)



