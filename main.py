from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/start-trial', methods=['POST'])
def start_trial():
    email = request.form.get('email')
    if email:
        print(f"New trial started for: {email}")
        flash("Thank you for signing up!")
        return redirect('/')
    else:
        flash("Please enter a valid email.")
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
