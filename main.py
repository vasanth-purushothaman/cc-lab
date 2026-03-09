from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Nth Largest Number</title>
</head>
<body>
    <h2>Find Nth Largest Number</h2>
    <form method="post">
        <label>Enter numbers (comma separated):</label><br>
        <input type="text" name="numbers" required><br><br>

        <label>Enter N:</label><br>
        <input type="number" name="n" required><br><br>

        <button type="submit">Find</button>
    </form>

    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
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
            numbers = list(map(int, request.form["numbers"].split(",")))
            n = int(request.form["n"])

            if n > len(numbers) or n <= 0:
                error = "N must be between 1 and the number of elements"
            else:
                numbers = sorted(set(numbers), reverse=True)
                result = numbers[n - 1]

        except Exception:
            error = "Invalid input. Please enter numbers correctly."

    return render_template_string(HTML, result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
