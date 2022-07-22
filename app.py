from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        return(render_template("index.html", result1=r1, result2=r2))
    else:
        return(render_template("index.html", result1="WAITING", result2="WAITING"))

if __name__ == "__main__":
    app.run()