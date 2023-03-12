#!/usr/bin/python3
"""Unit tests for amenity model"""

import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Defines unit tests for amenity model"""

    def setUp(self):
        """set up tests"""
        FileStorage._FileStorage__file_path = "test.json"
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """tear down tests"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_inherits_base_model(self):
        """Test if Amenity inherits BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_public_instance_attributes(self):
        """Test public instance attributes"""
        amenity = Amenity()

        self.assertIsInstance(amenity.name, str)
        self.assertEqual(amenity.name, "")
        amenity.name = "Air conditioning"
        self.assertEqual(amenity.name, "Air conditioning")
