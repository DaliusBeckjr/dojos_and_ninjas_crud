from flask_app import app 
# since we brought in the app we can use our route decorator
from flask import render_template, session, request, redirect, session
from flask_app.models import dojo # trip

# root route
@app.route('/')
def root():
    return redirect('/dojos/dashboard')

#dojos section:
@app.route('/dojos/dashboard')
def dojo_dashboard():
    dojos = dojo.Dojo.get_all_dojos()
    print(dojos)
    return render_template('dojo_dashboard.html', all_dojos = dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    data = {
        'name' : request.form['name']
    }
    dojo.Dojo.save_dojos(data)
    return redirect('/dojos/dashboard')
