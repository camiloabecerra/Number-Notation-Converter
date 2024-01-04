from flask import Flask, render_template, request
from roman_numerals import to_arabic, to_roman

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/roman_to_arabic")
def roman_to_arabic():
    return render_template("roman_to_arabic.html")

@app.route("/arabic_to_roman")
def arabic_to_roman():
    return render_template("arabic_to_roman.html")

@app.route("/roman_to_arabic_result", methods=["POST", "GET"])
def roman_to_arabic_result():
    output = request.form.to_dict()
    roman_number = output["roman"]
    try:
        arabic = to_arabic(roman_number)
        return render_template("roman_to_arabic.html", arabic=arabic)
    except ValueError as e:
        return render_template("roman_to_arabic.html", error=e)

@app.route("/arabic_to_roman_result", methods=["POST", "GET"])
def arabic_to_roman_result():
    output = request.form.to_dict()
    arabic_number = output["arabic"]
    try:
        roman = to_roman(int(arabic_number))
        return render_template("arabic_to_roman.html", roman=roman)
    except ValueError as e:
        return render_template("arabic_to_roman.html", error=e)

if __name__ == '__main__':
    app.run(debug= True, port="5001")