from apps.entities.controllers import PersonController
from apps.entities.schemas import Person
from apps.entities.utils import create_generic_entity


class PersonServices:

    def __init__(self):
        self.controller = PersonController()

    def create_person(self, data):
        pass

    def get_entity(self, oid: str) -> Person:
        """
        Search Person in the database using oid.

        Parameters:
            oid: ID of the object that will be searched

        returns:
            Person or none if it does not exist
        """

        return self.controller.object(oid)

    def get_entity_by_identifier(self, identifier: str) -> list:
        """
        Get person in the database using identifier.

        Parameters:
            identifier: Official Document number of the object that will be searched

        returns:
            Person or none if it does not exist
        """

        return self.controller.filter({"identifier": identifier})

    def filter_entity_by_name(self, name: str) -> list:
        """
        Filter entity in the database using name.

        Parameters:
            name: Name of the object that will be searched

        returns:
            Person or none if it does not exist
        """

        return self.controller.filter({"name": name})

    def filter_entity_are_father(self) -> list:
        """
        Filter entities in the database that are father.

        returns:
            List of parents registered in the system
        """

        return self.controller.filter({"children": 1})

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


