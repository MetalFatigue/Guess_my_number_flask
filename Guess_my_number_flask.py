from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=['GET,POST'])
def guess_my_number():
    if request.method == 'GET':
        return render_template('START.html')
    elif request.method == 'POST':
        min_val = int(request.form.get('min_val'))
        max_val = int(request.form.get('max_val'))
        guess = int((min_val + max_val)/2)
        user_answer = request.form.get('user_answer')
        if user_answer == "YOU WIN":
            return render_template('WIN.html', guess=guess)
        elif user_answer == 'TOO SMALL':
            min_val = guess
        elif user_answer == 'TOO BIG':
            max_val = guess

        return render_template('GAME.html', min_val=min_val, max_val=max_val, guess=guess)


if __name__ == "__main__":
    app.run(debug=True)
