from flask import Flask , render_template , request , redirect , session

app = Flask(__name__)

app.secret_key = 'sunabakoza'

@app.route('/')
def toppage():
    return render_template('top.html')

@app.route('/favorite')
def favorite():
    return render_template('favorite.html')

if __name__ == "__main__":
    app.run()