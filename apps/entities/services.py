from apps.entities.models import Person
from apps.entities.utils import create_generic_entity


class PersonServices:

    def create_person(self, data):
        pass

    def search_person(self, oid):
        pass

    def filter_people(self, query):
        pass

    def update_person(self, oid, data):
        pass

    def delete_person(self, oid):
        pass

    def search_people_who_have_children(self):
        pass

    def generate_person(self):
        data = create_generic_entity()
        person = Person(**data)
        return person


