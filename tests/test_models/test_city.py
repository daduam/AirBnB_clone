#!/usr/bin/python3
"""Unit tests for city model"""

import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.city import City


class TestCity(unittest.TestCase):
    """Defines unit tests for city model"""

    def setUp(self):
        """set up tests"""
        FileStorage._FileStorage__file_path = "test.json"
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """tear down tests"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_inherits_base_model(self):
        """Test if City inherits BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_public_instance_attributes(self):
        """Test public instance attributes"""
        city = City()

        self.assertIsInstance(city.state_id, str)
        self.assertEqual(city.state_id, "")
        city.state_id = "76e3063b-3397-47bb-8351-fe928050c982"
        self.assertEqual(city.state_id, "76e3063b-3397-47bb-8351-fe928050c982")

        self.assertIsInstance(city.name, str)
        self.assertEqual(city.name, "")
        city.name = "Austin"
        self.assertEqual(city.name, "Austin")
