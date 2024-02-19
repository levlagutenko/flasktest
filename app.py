from flask import Flask, render_template, request

app = Flask(__name__) ##инициализируем имя файла app.py, как имя основного файл приложении


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        card_id = request.form['card_id']
        # проверка логина и пароля
        print(card_id)
        return 'Вы вошли в систему!'
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run()