#!/usr/bin/python3
"""Unit tests for place model"""

import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place


class TestPlace(unittest.TestCase):
    """Defines unit tests for place model"""

    def setUp(self):
        """set up tests"""
        FileStorage._FileStorage__file_path = "test.json"
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """tear down tests"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_inherits_base_model(self):
        """Test if Place inherits BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_public_instance_attributes(self):
        """Test public instance attributes"""
        place = Place()

        self.assertIsInstance(place.city_id, str)
        self.assertEqual(place.city_id, "")
        place.city_id = "76e3063b-3397-47bb-8351-fe928050c982"
        self.assertEqual(place.city_id, "76e3063b-3397-47bb-8351-fe928050c982")

        self.assertIsInstance(place.user_id, str)
        self.assertEqual(place.user_id, "")
        place.user_id = "76e3063b-3397-47bb-8351-fe928050c982"
        self.assertEqual(place.user_id, "76e3063b-3397-47bb-8351-fe928050c982")

        self.assertIsInstance(place.name, str)
        self.assertEqual(place.name, "")
        place.name = "Condo in Austin"
        self.assertEqual(place.name, "Condo in Austin")

        self.assertIsInstance(place.description, str)
        self.assertEqual(place.description, "")
        place.description = "Condo in Austin"
        self.assertEqual(place.description, "Condo in Austin")

        self.assertIsInstance(place.number_rooms, int)
        self.assertEqual(place.number_rooms, 0)
        place.number_rooms = 2
        self.assertEqual(place.number_rooms, 2)

        self.assertIsInstance(place.number_bathrooms, int)
        self.assertEqual(place.number_bathrooms, 0)
        place.number_bathrooms = 3
        self.assertEqual(place.number_bathrooms, 3)

        self.assertIsInstance(place.max_guest, int)
        self.assertEqual(place.max_guest, 0)
        place.max_guest = 1
        self.assertEqual(place.max_guest, 1)

        self.assertIsInstance(place.price_by_night, int)
        self.assertEqual(place.price_by_night, 0)
        place.price_by_night = 250
        self.assertEqual(place.price_by_night, 250)

        self.assertIsInstance(place.latitude, float)
        self.assertEqual(place.latitude, 0.0)
        place.latitude = 30.2672
        self.assertEqual(place.latitude, 30.2672)

        self.assertIsInstance(place.longitude, float)
        self.assertEqual(place.longitude, 0.0)
        place.longitude = 97.7431
        self.assertEqual(place.longitude, 97.7431)

        self.assertIsInstance(place.amenity_ids, list)
        self.assertEqual(place.amenity_ids, [])
        place.amenity_ids = ["76e3063b-3397-47bb-8351-fe928050c982"]
        self.assertEqual(place.amenity_ids,
                         ["76e3063b-3397-47bb-8351-fe928050c982"])
