#!/usr/bin/python3
"""Unit tests for review model"""

import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.review import Review


class TestReview(unittest.TestCase):
    """Defines unit tests for review model"""

    def setUp(self):
        """set up tests"""
        FileStorage._FileStorage__file_path = "test.json"
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """tear down tests"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_inherits_base_model(self):
        """Test if Review inherits BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_public_instance_attributes(self):
        """Test public instance attributes"""
        review = Review()

        self.assertIsInstance(review.place_id, str)
        self.assertEqual(review.place_id, "")
        review.place_id = "76e3063b-3397-47bb-8351-fe928050c982"
        self.assertEqual(review.place_id,
                         "76e3063b-3397-47bb-8351-fe928050c982")

        self.assertIsInstance(review.user_id, str)
        self.assertEqual(review.user_id, "")
        review.user_id = "76e3063b-3397-47bb-8351-fe928050c982"
        self.assertEqual(review.user_id,
                         "76e3063b-3397-47bb-8351-fe928050c982")

        self.assertIsInstance(review.text, str)
        self.assertEqual(review.text, "")
        review.text = "This condo is wack"
        self.assertEqual(review.text, "This condo is wack")
