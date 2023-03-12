#!/usr/bin/python3
"""Unit tests for user model"""

import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestUser(unittest.TestCase):
    """Defines unit tests for user model"""

    def setUp(self):
        """set up tests"""
        FileStorage._FileStorage__file_path = "test.json"
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """tear down tests"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_inherits_base_model(self):
        """Test if User inherits BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_public_instance_attributes(self):
        """Test public instance attributes"""
        user = User()

        self.assertIsInstance(user.email, str)
        self.assertEqual(user.email, "")
        user.email = "user@alx.com"
        self.assertEqual(user.email, "user@alx.com")

        self.assertIsInstance(user.password, str)
        self.assertEqual(user.password, "")
        user.password = "password"
        self.assertEqual(user.password, "password")

        self.assertIsInstance(user.first_name, str)
        self.assertEqual(user.first_name, "")
        user.first_name = "Kojo"
        self.assertEqual(user.first_name, "Kojo")

        self.assertIsInstance(user.last_name, str)
        self.assertEqual(user.last_name, "")
        user.last_name = "Ojok"
        self.assertEqual(user.last_name, "Ojok")
