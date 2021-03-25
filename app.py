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

@app.route('/my_account', methods=['GET'])
def my_account():
    return render_template('my_account.html')

@app.route('/my_account', methods=['POST'])
def make_account():
    name = request.form.get("name")
    # ↑()の中は拾ってくる"入力欄"の名前(name="○○"の丸の部分)を入れる
    mailaddress = request.form.get("mailaddress")
    pass1 = request.form.get("pass1")
    pass2 = request.form.get("pass2")
    if pass1 == pass2:
        conn = sqlite3.connect('diy.db')
        # ↑()の中はデータベースの名前
        c = conn.cursor()
        c.execute("INSERT INTO user_list VALUES(null, ?, ?, ?, ?)", (name, mailaddress, pass1, pass2))
        conn.commit()
        conn.close()
        return redirect('/my_user')
    else:
        return render_template('my_account.html')
        #redirectは（）のなかにapp.pyで定義したリンク名を入れるのに対し、
        #render_templateは()のなかにhtml名を入れる。
        #両者の違いは、html(render_tenplate)はどんな人が見ても同じページが表示されるのに対し、
        #app.pyで定義したリンク名（redirect）はデーターベースを繋げられることで
        #各ユーザーごとのページを表示することができる


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
    #(GETとPOSTで名前は変える)
    img = request.files['img_post'].read()
    task = request.form.get("task")
    # ↑()の中は拾ってくる"入力欄"の名前(name)を入れる
    conn = sqlite3.connect('diy.db')
    # ↑()の中はデータベースの名前
    c = conn.cursor()
    c.execute("INSERT INTO post_list VALUES(null, ?, ?, ?)", (0, task, img))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
