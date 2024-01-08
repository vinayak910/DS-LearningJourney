from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')


@app.route('/postman_data', methods=['POST'])
def math_operation():
    if (request.method == 'POST'):
        ops = request.json['ops']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if ops == "add":
            result = f"The sum of {num1} and {num2} is {num1 + num2}"
        elif ops == "substract":
            result = f"The substraction of {num1} and {num2} is {num1 - num2}"
        elif ops == "multiply":
            result = f"The multiplication of {num1} and {num2} is {num1 * num2}"
        elif ops == "divide":
            result = f"The division of {num1} and {num2} is {num1 / num2}"
        return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
