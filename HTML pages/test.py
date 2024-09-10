from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        try:
            return render_template("test.html", result=request.form['sub_button'])
        except:
            return render_template("test.html",result="ERROR")
    return render_template("test.html", result="none")
@app.route('/homepage',methods=['GET','POST'])
    
if __name__=='__main__':
    app.run(debug=True)
