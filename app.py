from flask import Flask,request,jsonify,url_for,render_template 
from textsummarization import summarize



app=Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/',methods=['POST', 'GET'])
def summary():
    if request.method == 'POST':
        text=request.form.get('text')
        if text == "":
            return render_template('home.html')
        t=request.form.get('lang')
        stext=summarize(text,t)
        return render_template('home.html',summarized_text='{}'.format(stext[0]),filename='{}'.format(stext[1]),text='{}'.format(text))


if((__name__)=='__main__'):
    app.run(debug=True)
