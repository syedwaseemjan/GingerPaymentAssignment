from flask import Blueprint, render_template, redirect, flash, url_for, request
from gingerpayments.frontend import route
from flask_login import current_user, login_required, login_user, logout_user
from gingerpayments.decorators import logout_required
from gingerpayments.forms import LoginForm
from gingerpayments.forms import NewGroupForm, UpdateGroupForm


bp = Blueprint('groups', __name__)


@bp.route('/new-group')
def new():
	form = NewGroupForm()
	return render_template('groups/new_group.html', form=form)

@bp.route('/groups/<int:group_id>')
def show(group_id):
	return render_template('groups/show.html')

