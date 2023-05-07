from flask import Flask, render_template, redirect, request
import dojo, ninja 
app = Flask(__name__)


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

#ninjas section
@app.route('/ninjas/dashboard')
def ninjas_dashboard():
    ninjas = ninja.Ninja.get_all_ninjas()
    print(ninjas)
    return render_template('ninjas_dashboard.html', all_ninjas = ninjas)





if __name__ == "__main__":
    app.run(debug=True, port= 5001)