from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/grade', methods=['POST'])
def grade():
    code = request.form['code']

    conn = sqlite3.connect('code.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO submissions (code) VALUES (?)", (code,))
    conn.commit()
    conn.close()

    score = len(code)

    return 'Your code score is: {}'.format(score)
