#!/usr/bin/python3
"""Unit tests for state model"""

import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State


class TestState(unittest.TestCase):
    """Defines unit tests for state model"""

    def setUp(self):
        """set up tests"""
        FileStorage._FileStorage__file_path = "test.json"
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """tear down tests"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_inherits_base_model(self):
        """Test if State inherits BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_public_instance_attributes(self):
        """Test public instance attributes"""
        state = State()

        self.assertIsInstance(state.name, str)
        self.assertEqual(state.name, "")
        state.name = "Texas"
        self.assertEqual(state.name, "Texas")
