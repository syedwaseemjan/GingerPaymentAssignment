from flask import Blueprint, render_template, redirect, flash, url_for, request
from addressbook.frontend import route
from flask_login import current_user, login_required, login_user, logout_user
from addressbook.decorators import logout_required
from addressbook.forms import LoginForm
from addressbook.forms import NewPersonForm, UpdatePersonForm

bp = Blueprint('persons', __name__)


@bp.route('/new-person', methods=['GET','POST'])
def new():
	form = NewPersonForm()
	if form.validate_on_submit():
		return render_template('persons/new_person.html', form=form)
	return render_template('persons/new_person.html', form=form)

@bp.route('/persons/<int:person_id>')
def show(person_id):
	return render_template('persons/show.html')