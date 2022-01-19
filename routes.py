from app import app 
from flask import render_template
from app.forms import AddContactForm

@app.route("/home")
def hello():
    return "Hello"


@app.route('/add', methods=["GET","POST"])
def addcontact():
    form = AddContactForm()
    # if form.validate_on_submit():
    #     first_name = form.first_name.data
    #     last_name = form.last_name.data
    #     phone_number = form.phone_number.data
    #     address = form.address.data
    #     print(first_name, last_name, phone_number, address)
    return render_template('add.html', form=form)
