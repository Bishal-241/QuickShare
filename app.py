from flask import Flask,request, url_for, render_template as render , redirect

from api import dOprator
app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def main():                                                                                 #MAIN_ENTRANCE_PAGE
    if request.method == 'POST':
        txt = request.form['message']
        password = request.form['pass']
        if(password == None):
            password = ""                                                                   #HANDELING_NO_PASSWORD_CASE
        try:
            rtn = dOprator.insertData(txt,password)                                         #RETURN DATA ENTERED AND ID
            return f'Your entered data : {rtn} ; try <a href></a>' 
        except:
            return "Error during internal execution"
    else:
        return render('index.html')


@app.route("/<id>/<pswd>")
def dPage(id,pswd):                                                                         #PAGE_THAT_ALLOWS_AFTER_ENTRY_OPERATIONS
    data = {
        'text' : None,
        'id'    :id,
        'password' : pswd,
    }
    try : 
        val = dOprator.retriveData(id,pswd)
    except:
        data['text'] = "Internal Error occured"
    data['text'] = val
    return render('dPage.html',txt = data['text'])
        


@app.route('/<text>')
def test(text):
    return f'Entered text:{text}'

if(__name__ == "__main__"):
    app.run(debug=True, port=5000)



