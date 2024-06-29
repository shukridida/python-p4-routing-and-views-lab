from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:no>')
def count_number(no):
    count =f''
    for n in range(no):
      count += f'{n}/n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str (num1 + num2)
    
    elif operation == '-':
        return  str(num1 - num2)
    
    elif operation == '*':
        return  str (num1 * num2)
    
    elif operation == 'div':
        return str (num1 / num2)
    
    elif operation == '%':
        return str   (num1 % num2)
    
    return 'operation not detected. use one of this :- + * %'

if __name__ == '__main__':
    app.run(debug=True)
