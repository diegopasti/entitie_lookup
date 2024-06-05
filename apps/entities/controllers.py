from apps.entities.schemas import Person
from utils.database import Mongo


class PersonController:

    def __init__(self):
        self.mongo = Mongo("entity-lookup")
        self.mongo.use_collection("entities")

    """def all(self):
        ""
        Returns all saved records or an empty list if there are no records

        returns:
            List with saved records or empty list
        ""

        return self.search(query={})
        """

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
        #return self.search(query=query)
        cursor = self.mongo.filter(query, exclude, sort, limit)
        return [Person(**item) for item in cursor]

    def update(self, oid: str, data: dict):
        """
        Search document in the database using object oid.
        If the dictionary is empty, the complete list is returned.

        Parameters:
            oid: Dictionary with fields used for consultation
            data: Dictionary with new values

        returns:
            Person updated or none if it does not exist
        """

        try:
            return Person(**self.mongo.update(oid, data))

        except TypeError:
            return None

    def insert(self, data: dict):
        """
        Create a new Person into database

        Parameters:
            data: Dictionary with object data

        returns:
            Person object saved in the database or None
        """

        try:
            new_person_oid = str(self.mongo.insert(data).inserted_id)
            return self.object(new_person_oid)

        except TypeError:
            return None

    def delete(self, oid: str):
        """
        Delete document in the database using object oid.

        Parameters:
            oid: Identifier of the object to be changed

        returns:
            Number of objects deleted, zero if there is no object with this oid
        """

        return self.mongo.delete(oid).deleted_count