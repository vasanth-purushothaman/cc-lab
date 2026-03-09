from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Generate N Even Numbers</title>
</head>
<body>
    <h2>Generate First N Even Numbers</h2>
    <form method="post">
        <label>Enter N:</label><br>
        <input type="number" name="n" required><br><br>

        <button type="submit">Generate</button>
    </form>

    {% if result %}
        <h3>Even Numbers: {{ result }}</h3>
    {% endif %}

    {% if error %}
        <h3 style="color:red;">{{ error }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            n = int(request.form["n"])

            if n <= 0:
                error = "N must be greater than 0"
            else:
                result = [2 * i for i in range(1, n + 1)]

        except Exception:
            error = "Invalid input."

    return render_template_string(HTML, result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)