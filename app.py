from flask import Flask,request, url_for, render_template as render , redirect

from api import dOprator
app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def main():                                                                                 #MAIN_ENTRANCE_PAGE
    if request.method == 'POST':
        txt = request.form['message']
        password = request.form['pass']
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
        'text' : None
    }
    try : 
        data['text'] = dOprator.retriveData(id,pswd)
    except:
        data['text'] = "Internal Error occured"
    return f"Here is your data:<br>{data['text']}"

@app.route('/<text>')
def test(text):
    return f'Entered text:{text}'

if(__name__ == "__main__"):
    app.run(debug=True, port=5000)



