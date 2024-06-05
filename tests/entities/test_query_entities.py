import json
import unittest
import requests

from apps.entities.utils import create_generic_entity


class SimpleQueryTestCase(unittest.TestCase):

    def setUp(self):
        print("\nRunning setUp method...")
        person = create_generic_entity()
        response = requests.get("http://127.0.0.1:8000/personx/", data=json.dumps(person, default=str))
        print("VEJA O QUE FOI CRIADO E O ID:", response, response.content)


    def tearDown(self):
        print("Running tearDown method...")

    def test_simple_query_case(self):
        print("VOU TESTAR")
        #response = requests.get("http://127.0.0.1:8000/person/664faca248d62fb63eb4eb53")
        #print("CREATION:", response.json())
        #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    runner = unittest.TextTestRunner(verbosity=3)
    unittest.main()
