from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        test_string = request.form.get("test_string")
        regex_pattern = request.form.get("regex_pattern")
        matched_strings = perform_regex_matching(test_string, regex_pattern)
        return redirect(url_for("results", test_string=test_string, regex_pattern=regex_pattern, matched_strings=matched_strings))
    return render_template("index.html")

@app.route("/results")
def results():
    test_string = request.args.get("test_string")
    regex_pattern = request.args.get("regex_pattern")
    matched_strings = request.args.get("matched_strings").split(",") if request.args.get("matched_strings") else []
    return render_template("results.html", test_string=test_string, regex_pattern=regex_pattern, matched_strings=matched_strings)

def perform_regex_matching(test_string, regex_pattern):
    matches = re.findall(regex_pattern, test_string)
    return matches

if __name__ == "__main__":
    app.run(debug=True)
