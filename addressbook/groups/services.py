from addressbook.extensions import Service
from addressbook.models import Group
from addressbook.exceptions import AddressBookError


class GroupsService(Service):
    __model__ = Group

    def __init__(self, *args, **kwargs):
        super(GroupsService, self).__init__(*args, **kwargs)

    def add_person(self, group, user):
        if user in group.persons:
            raise AddressBookError(u'Person exists')
        group.persons.append(user)
        return self.save(group), user

    def remove_person(self, group, user):
        if user not in group.persons:
            raise AddressBookError(u'Invalid person')
        group.persons.remove(user)
        return self.save(group), user

    def add_group(self, group, user):
        if user in group.persons:
            raise AddressBookError(u'Person exists')
        group.persons.append(user)
        return self.save(group), user

    def remove_group(self, group, user):
        if user not in group.persons:
            raise AddressBookError(u'Invalid person')
        group.persons.remove(user)
        return self.save(group), user
