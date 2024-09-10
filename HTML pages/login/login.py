from flask import *
#Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        try:
            if request.form['input'] == 'create new user':
                return redirect('login-create-user')
            elif request.form['input'] == 'login':
                return redirect('login-user')
                
        except:
            return render_template('home.html')
    return render_template('home.html')
    


@app.route('/login-create-user', methods=['GET','POST'])
def main_create_user():
    if request.method == 'POST':
        if request.form['button'] == "input information":
            conn=sqlite3.connect('logindatabase.db')
            db = conn.cursor()
            name = str(request.form['name'])
            email = str(request.form['email'])
            password1 = str(request.form['password1'])
            password2 = str(request.form['password2'])
            print(name,email,password1,password2)
            if len(name) == 0:
                return render_template('createUser.html', ERROR="Please enter a name")
            if (("@" in email) and ((email[0] and email[len(email)-1]) != "@")) == False:
                return render_template('createUser.html', ERROR="Email is not valid")
            if password1 != password2:
                return render_template('createUser.html', ERROR="The two passswords do not match")
            else:
                db.execute("INSERT INTO Users (name,email,password) VALUES (?,?,?)",(name,email,password1));
                conn.commit()
                conn.close()
                return redirect('home')
        elif request.form['button'] == "Go Back":
            return redirect('home')
    return render_template('createUser.html', ERROR = "")

@app.route('/login-user',methods=['GET','POST'])
def main_log_in():
    if request.method == 'POST':
        if request.form['button'] == "Submit Information":
            print("YAAA")
            LoginEmail = str(request.form['EnterEmail'])
            LoginPass = str(request.form['EnterPassword'])
            conn=sqlite3.connect('logindatabase.db')
            db = conn.cursor()
            
        elif request.form['button'] == "Go Back":
            return redirect('home')
    return render_template('LoginUser.html',invalid="")

if __name__ == '__main__':
    app.run(debug = True)
            
    
    
