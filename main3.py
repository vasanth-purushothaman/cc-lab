from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Matrix Multiplication</title>
</head>
<body>

<h2>Matrix Multiplication (2x2)</h2>

<p><b>Matrix A:</b> {{ A }}</p>
<p><b>Matrix B:</b> {{ B }}</p>
<p><b>Result:</b> {{ result }}</p>

</body>
</html>
"""

@app.route("/")
def multiply():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    result = [[sum(A[i][k] * B[k][j] for k in range(2))
              for j in range(2)]
              for i in range(2)]

    return render_template_string(HTML, A=A, B=B, result=result)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
