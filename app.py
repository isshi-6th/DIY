from flask import Flask , render_template , request , redirect , session
import sqlite3

app = Flask(__name__)

app.secret_key = 'sunabakoza'

@app.route('/')
def toppage():
    return render_template('top.html')

@app.route('/favorite')
def favorite():
    return render_template('favorite.html')

@app.route('/my_login')
def my_login():
    return render_template('my_login.html')

@app.route('/my_account')
def my_account():
    return render_template('my_account.html')

@app.route('/my_user')
def my_user():
    return render_template('my_user.html')    

@app.route('/diy')
def diy():
    return render_template('diy.html')

@app.route('/creator')
def creator():
    return render_template('creator.html')

@app.route('/post', methods=["GET"])
def post():
    return render_template('post.html')

@app.route('/post', methods=['POST'])
def add_post():
    task = request.form.get("task")
    # ↑()の中は拾ってくる"入力欄"の名前を入れる
    conn = sqlite3.connect('diy.db')
    # ↑()の中はデータベースの名前
    c = conn.cursor()
    c.execute("INSERT INTO post_list VALUES(null, ?, ?)", (0, task))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == "__main__":
    app.run()    