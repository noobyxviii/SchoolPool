from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def main():
  return render_template("index.html")

@app.route('/cranbrook')
def cranbrook():
  return render_template("cranbrook.html")

@app.route('/riverview')
def riverview():
  return render_template("riverview.html")

@app.route('/add')
def add():
  return render_template("add.html")

app.run(host='0.0.0.0', port=8080, debug=True)
