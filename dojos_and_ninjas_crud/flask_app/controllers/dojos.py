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


# show page
@app.route('/dojos/show/<int:id>')
def show_dojo(id):
    data = {
        'id': id
    }
    one_dojo = dojo.Dojo.get_ninjas_with_dojo(data)
    print(one_dojo)
    return render_template('show_dojo.html', one_dojo = one_dojo)



# show page
# @app.route('/dojos/show/<int:id>')
# def show_dojo(id):
#     data = {
#         'id' : id 
#     }
#     dojos = dojo.Dojo.get_ninjas_with_dojo(data)
#     print(dojos)
#     return render_template('show_dojo.html', one_dojo = dojos)

