import logging

from bson import ObjectId
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from conf.settings import MONGODB_URL


class Database:

    def object(self, oid: str):
        """
        Search object with oid informed

        Parameters:
            oid: Identifier of the searched object

        returns:
            Object with oid provided or none if it does not exist
        """

        pass

    def search(self, query=dict):
        """
        Search records in the database using query parameters using dictionary with fields and values.
        If the dictionary is empty, the complete list is returned.

        Parameters:
            query: Dictionary with fields used for consultation

        returns:
            document: List with documents corresponding to the searched fields
        """

        pass

    def insert(self, data):
        """
        Create a new object into database

        Parameters:
            data: Dictionary with object data

        returns:
            oid of saved object saved in the database
        """

        pass

    def update(self, oid, data):
        """
        Updates an object's data in the database

        Parameters:
            oid: Identifier of the object to be changed
            data: Dictionary with object data

        returns:
            result of the operation, true if changed successfully or false
        """

        pass

    def delete(self, oid):
        """
        Delete an object's data in the database

        Parameters:
            oid: Identifier of the object to be changed

        returns:
            result of the operation, true if deleted successfully or false
        """

        pass


class Mongo(Database):

    def __init__(self, database: str):
        """ Initialize Mongo database client with a database """

        self.database = None
        self.collection = None
        self.cursor = None

        try:
            self.client = MongoClient(MONGODB_URL)
            self.connect(database)

        except ConnectionFailure as exception:
            logging.error("Connection to Mongo Database Failed: %s", exception)

    def connect(self, database: str):
        """ Defines the active database """

        self.database = self.client[database]

    def use_collection(self, name: str):
        """ Defines the active collection """

        self.collection = self.database.get_collection(name)

    def object(self, oid: str):
        """
        Search document in the database using object oid.
        If the dictionary is empty, the complete list is returned.

        Parameters:
            oid: Dictionary with fields used for consultation

        returns:
            Document with oid provided or none if it does not exist
        """

        return self.collection.find_one({"_id": ObjectId(oid)})

    def filter(self, query=dict, exclude: dict | None = None, sort: list | None = None, limit: int = 0):
        """
        Search objects in the database using fields and values in a dictionary format.
        If the dictionary is empty, the complete list is returned.

        Parameters:
            query: Dictionary with fields used for consultation
            exclude: Dictionary with fields that will not be returned
            sort: List with tuples, ex: sort=[("name", pymongo.DESCENDING), ("age", pymongo.ASCENDING)]
            limit: Limit results, default zero for unlimited

        returns:
            List with documents corresponding to the searched fields
        """

        args = {"limit": limit}

        if exclude:
            args["projection"] = exclude

        if sort:
            args["sort"] = sort

        return self.collection.find(query, **args)

    def insert(self, data):
        """
        Create a new object into database

        Parameters:
            data: Dictionary with object data

        returns:
            oid of saved object saved in the database
        """

        return self.collection.insert_one(data.dict())

    def update(self, oid, data):
        """
        Updates an object's data in the database

        Parameters:
            oid: Identifier of the object to be changed
            data: Dictionary with object data

        returns:
            result of the operation, true if changed successfully or false
        """

        new_values = {"$set": data}
        return self.collection.find_one_and_update({"_id": ObjectId(oid)}, new_values)

    def delete(self, oid):
        """
        Delete an object's data in the database

        Parameters:
            oid: Identifier of the object to be changed

        returns:
            result of the operation, true if deleted successfully or false
        """

        return self.collection.delete_one({"_id": ObjectId(oid)})
