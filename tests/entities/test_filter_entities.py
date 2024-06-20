import json
import unittest
import requests

from apps.entities.controllers import PersonController
from apps.entities.utils import create_generic_entity
from conf.settings import BASE_URL


class EntitiesControllerTestCase(unittest.TestCase):
    def setUp(self):
        data = create_generic_entity()
        self.controller = PersonController()
        self.entity = self.controller.insert(data)

    def tearDown(self):
        self.controller.delete({"name": self.entity.name})

    def test_filter_case(self):
        query = {"name": self.entity.name}
        response = self.controller.filter(query)
        self.assertIn(self.entity, response)


class EntitiesApiRestTestCase(unittest.TestCase):

    def setUp(self):
        self.person = create_generic_entity()
        self.query = {"name": self.person["name"]}
        requests.post(
            url=f"{BASE_URL}/api/entities/person",
            data=json.dumps(self.person)
        )

    def tearDown(self):
        requests.delete(
            url=f"{BASE_URL}/api/entities/person",
            data=json.dumps(self.query)
        )

    def test_filter_case(self):
        response = requests.get(
            url=f"{BASE_URL}/api/entities/person",
            data=json.dumps(self.query)
        )

        self.assertEqual(self.person["name"], response.json()[0]["name"])


if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main()
