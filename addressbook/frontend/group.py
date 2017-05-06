from flask import Blueprint, render_template
from addressbook.forms import NewGroupForm


bp = Blueprint('groups', __name__)


@bp.route('/new-group')
def new():
    form = NewGroupForm()
    return render_template('groups/new_group.html', form=form)


@bp.route('/groups/<int:group_id>')
def show(group_id):
    return render_template('groups/show.html')
