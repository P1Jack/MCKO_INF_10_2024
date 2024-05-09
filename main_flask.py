from flask import Flask, url_for, request, render_template, flash
from math_funcs import number1, number5

app = Flask(__name__)
app.config['SECRET_KEY'] = 'drist_secret_key'


@app.route('/', methods=['GET'])
def main():
    return render_template('first.html', style=url_for('static', filename='css/style.css'))


@app.route('/num1', methods=['GET'])
def num1():
    return render_template('num1.html', style=url_for('static', filename='css/style.css'))


@app.route('/num1', methods=['POST'])
def num1p():
    num1 = request.form['num1'].replace('.', ',')
    base1 = int(request.form['base1'])
    num2 = request.form['num2'].replace('.', ',')
    base2 = int(request.form['base2'])
    res_base = request.form['res_base']
    sign = request.form['sign']
    try:
        answer = number1(num1, base1, num2, base2, res_base, sign)
    except ValueError or TypeError:
        flash('Неправильный ввод данных')
        return render_template('num1.html', style=url_for('static', filename='css/style.css'))
    flash('Ваш ответ: ' + answer)
    return render_template('num1.html', style=url_for('static', filename='css/style.css'))


@app.route('/num5', methods=['GET'])
def num5():
    return render_template('num5.html', style=url_for('static', filename='css/style.css'))


@app.route('/num5', methods=['POST'])
def num5p():
    num = request.form['num'].replace(',', '.')
    d = request.form['d']
    format1 = request.form['format1']
    base = request.form['base']
    try:
        answer = number5(float(num), int(d) if d else 127, int(format1) if format1 else 32, base)
    except ValueError or TypeError:
        flash('Неправильный ввод данных')
        return render_template('num5.html', style=url_for('static', filename='css/style.css'))
    flash('Ваш ответ: ' + answer)
    return render_template('num5.html', style=url_for('static', filename='css/style.css'))


if __name__ == '__main__':
    app.run(port=8888, host='127.0.0.1')