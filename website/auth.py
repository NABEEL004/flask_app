from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if '@' not in email:
            flash("Email must be greater than 4 characters", category = 'error')
        elif password1 < 7:
            flash("Password must be at least 7 characters.", category='error')
        elif password1 != password2:
            flash("Passwords do not match.", category='error')
        else:
            flash("Sign-up successful!", category = 'success')

    return render_template('sign-up.html')

