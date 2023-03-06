from flask import Flask , render_template
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)
@app.route('/')
def io():
    return render_template('r_main.html')
@app.route('/doritos')
def op():
    return render_template('orit.html')
@app.route('/maink')
def gy():
    return render_template('main.html')
@app.route('/random')
def gj():
    return render_template('random.html')
if __name__ == '__main__':
   app.run()