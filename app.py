from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('display_var'))

@app.route('/app')
def display_var():
    return render_template('display_var.html')

if __name__ == '__main__':
    app.run(debug=True)

