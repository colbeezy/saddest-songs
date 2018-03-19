from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/hello")
def hello():
    return render_template('message.html', message="Hello bran!")

if __name__ == "__main__":
    app.run()