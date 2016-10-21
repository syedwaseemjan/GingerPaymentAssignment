from flask import Blueprint, render_template, redirect, url_for, request
from gingerpayments.api import route
from flask_login import current_user, login_required
from gingerpayments.services import _groups, _persons
from gingerpayments.exceptions import GingerFormError, GingerError
from gingerpayments.forms import NewPersonForm, UpdatePersonForm

bp = Blueprint('person', __name__, url_prefix='/persons')

@route(bp, '/')
def list():
	"""Returns a list of user instances."""
	return _groups.all()

@route(bp, '/', methods=['POST'])
def new():
    """Creates a new person. Returns the new person instance."""
    form = NewPersonForm()
    if form.validate_on_submit():
        return _persons.create_person(form)
    raise GingerFormError(form.errors)

@route(bp, '/<person_id>')
def show(person_id):
    """Returns a person instance."""
    person = _persons.get_or_404(person_id)
    return _persons._serialize(person)

@route(bp, '/<person_id>/update', methods=['POST'])
def update(person_id):
    """Updates a person. Returns the updated person instance."""
    form = UpdatePersonForm()
    if form.validate_on_submit():
        return _persons.update(_persons.get_or_404(person_id), **request.json)
    raise GingerFormError(form.errors)

@route(bp, '/<person_id>/delete')
def delete(person_id):
    """Deletes a person. Returns a 204 response."""
    _persons.delete(_persons.get_or_404(person_id))
    return None, 204

@route(bp, '/<int:person_id>/groups')
def groups(person_id):
	return {}

@route(bp, '/search', methods=['POST'])
def search():
    """Returns a person instance."""
    text = request.form.get('text')
    person = _persons.search(text)
    if not person:
        raise GingerError("No Result Found")
    return _persons._serialize(person)


