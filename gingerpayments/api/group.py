from flask import Blueprint, render_template, redirect, url_for, request
from gingerpayments.api import route
from flask_login import current_user, login_required
from gingerpayments.services import _groups, _persons
from gingerpayments.exceptions import GingerFormError
from gingerpayments.forms import NewGroupForm, UpdateGroupForm

bp = Blueprint('groups', __name__, url_prefix='/groups')

@route(bp, '/')
def list():
	"""Returns a list of all groups instances."""
	return _groups.all()

@route(bp, '/', methods=['POST'])
def new():
    """Creates a new group. Returns the new group instance."""
    form = NewGroupForm()
    if form.validate_on_submit():
        return _groups.create(**request.json)
    raise GingerFormError(form.errors)

@route(bp, '/<group_id>')
def show(group_id):
    """Returns a group instance."""
    return _groups.get_or_404(group_id)

@route(bp, '/<group_id>/update', methods=['POST'])
def update(group_id):
    """Updates a group. Returns the updated group instance."""
    form = UpdateGroupForm()
    if form.validate_on_submit():
        return _groups.update(_groups.get_or_404(group_id), **request.json)
    raise GingerFormError(form.errors)

@route(bp, '/<group_id>/delete')
def delete(group_id):
    """Deletes a group. Returns a 204 response."""
    _groups.delete(_groups.get_or_404(group_id))
    return None, 204

@route(bp, '/<group_id>/persons/<user_id>')
def add_person(group_id, user_id):
    group, person = _groups.add_person(_groups.get_or_404(group_id),
                                         _persons.get_or_404(user_id))
    return group


@route(bp, '/<group_id>/persons/<user_id>/delete')
def remove_person(group_id, user_id):
    group, person = _groups.remove_person(_groups.get_or_404(group_id),
                                            _persons.get_or_404(user_id))
    return None, 204

