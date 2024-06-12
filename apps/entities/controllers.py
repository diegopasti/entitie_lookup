from apps.entities.schemas import Person
from apps.entities.utils import create_generic_entity
from utils.database import Mongo


class PersonController:

    def __init__(self):
        self.mongo = Mongo("entity-lookup")
        self.mongo.use_collection("entities")

    def object(self, oid: str):
        """
        Search Person in the database using oid.

        Parameters:
            oid: Identifier of the object to be changed

        returns:
            Person with oid provided or none if it does not exist
        """

        try:
            return Person(**self.mongo.object(oid))
        except TypeError:
            return None

    def filter(self, query: dict, exclude: dict | None = None, sort: list | None = None, limit: int = 0):
        """
        Search document in the database using object oid.
        If the dictionary is empty, the complete list is returned.

        Parameters:
            query: Dictionary with fields used for consultation
            exclude: Dictionary with fields that will not be returned
            sort: List with tuples, ex: sort=[("name", pymongo.DESCENDING), ("age", pymongo.ASCENDING)]
            limit: Limit results, default zero for unlimited

        returns:
            Document with oid provided or none if it does not exist
        """

        cursor = self.mongo.filter(query, exclude, sort, limit)
        return [Person(**item) for item in cursor]

    def update(self, query: dict, data: dict):
        """
        Updates one or more objects that meet the parameters sought with the values entered,
        Either by id or any other field that exists in the model.

        Parameters:
            query: A query that matches the documents to update
            data: Dictionary with new values

        returns:
            List of Person updated or none if it does not exist
        """

        try:
            return Person(**self.mongo.update(query, data))

        except TypeError:
            return None

    def insert(self, data: list):
        """
        Create one or more Person into database

        Parameters:
            data: List containing one or more Dictionary with data object

        returns:
            Person object saved in the database or None
        """

        return [self.object(oid) for oid in self.mongo.insert(data).inserted_ids]

    def delete(self, query: dict):
        """
        Delete one or more documents in the database using query parameters.

        Parameters:
            query: Identifier of the objects to be deleted

        returns:
            Number of objects deleted, zero if there is no object with this oid
        """

        return self.mongo.delete(query).deleted_count

    def generate(self, quant: int = 1):
        """
        Create one or more new random entity(s).

        :param quant: Quantity of new objects, default is 1.

        return: List of created objects
        """

        return self.insert([create_generic_entity() for item in range(quant)])
