from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import random

app = Flask(__name__)

user_data = pd.read_excel("Login_app/data/Educator.xlsx")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        if int(phone_number) in user_data['Phone'].values:
            # Generate an OTP and send it to the phone number (you need to implement this)
            otp = str(random.randint(1000, 9999))
            print(otp)
            # Redirect to OTP verification page
            print("Mobile number found OTP is sent")
            return redirect(url_for('verify_otp', phone_number=phone_number, otp=otp))
        else:
            return "This number is not registered in College/University"

    return render_template('login.html')

@app.route('/verify_otp/<phone_number>/<otp>', methods=['GET', 'POST'])
def verify_otp(phone_number, otp):
    if request.method == 'POST':
        entered_otp = request.form['otp']
        if int(entered_otp) == int(otp):
            print("Hello")
            return redirect(url_for('index'))
        else:
            print("Invalid OTP")
            return "Invalid OTP. Please try again."

    return render_template('verify_otp.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
