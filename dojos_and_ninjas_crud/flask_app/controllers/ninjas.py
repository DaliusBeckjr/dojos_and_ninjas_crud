from flask_app import app 
# since we brought in the app we can use our route decorator
from flask import render_template, session, request, redirect, session
from flask_app.models import ninja, dojo 
# adding dojo will give us access to the dojo.name 

#ninjas section
@app.route('/ninjas/dashboard')
def ninjas_dashboard():
    ninjas = ninja.Ninja.get_all_ninjas()
    print(ninjas)
    return render_template('ninjas_dashboard.html', all_ninjas = ninjas)

@app.route('/ninjas/new')
def new_ninja():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template('new_ninja.html', all_dojos = dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninjas():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo_id']
    }
    ninja.Ninja.save_ninjas(data)
    return redirect('/dojos/dashboard')

# edit/ update
@app.route('/ninjas/edit/<int:id>')
def edit_ninja(id):
    data = {
        'id' : id 
    }
    return render_template('edit_ninja.html', one_ninja = ninja.Ninja.get_one_ninja(data))

@app.route('/ninjas/update', methods=['POST'])
def update_ninja():
    ninja.Ninja.update_ninja(request.form)
    return redirect(f"/dojos/show/{request.form['id']}")

# delete
@app.route('/ninjas/delete/<int:id>')
def delete_ninja(id):
    data = {
        'id' : id 
    }
    ninja.Ninja.delete_ninja(data)
    return redirect(f"/dojos/show/{request.form['id']}")