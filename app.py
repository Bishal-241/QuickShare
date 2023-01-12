from flask import Flask, url_for, render_template as render
app = Flask(__name__)

#Testing sockets
# @app.route('/index/<subject>')
# def subject(subject):
#     return 'The value is: ' + subject

@app.route('/<id>')
def main(id):
    return render('index.html',i=id)

if(__name__ == "__main__"):
    app.run(debug=True, port=5000)



