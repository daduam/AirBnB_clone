#!/usr/bin/python3
"""Unit tests for base model module"""

import datetime
import unittest
import uuid

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines unit tests for BaseModel"""

    def test_public_instance_attributes(self):
        """Test public instance attributes"""
        bm = BaseModel()

        self.assertIsInstance(bm.id, str)
        val = uuid.UUID(bm.id, version=4)
        self.assertEqual(str(val), bm.id)

        self.assertIsInstance(bm.created_at, datetime.datetime)
        self.assertIsInstance(bm.updated_at, datetime.datetime)

    def test_str(self):
        """Test __str__ override"""
        bm = BaseModel()
        bm.name = "Testing base model"
        self.assertEqual(bm.__str__(),
                         "[BaseModel] ({}) {}".format(bm.id, bm.__dict__))

    def test_save(self):
        """Test save public instance method"""
        bm = BaseModel()
        old_date = bm.updated_at
        bm.save()
        new_date = bm.updated_at
        self.assertGreater(new_date, old_date)

    def test_to_dict(self):
        """Test to_dict public instance method"""
        bm = BaseModel()
        bm.name = "Testing base model"
        bmdict = bm.to_dict()
        self.assertListEqual(list(bmdict.keys()),
                             list(bm.__dict__.keys())+["__class__"])
        self.assertEqual(bmdict["__class__"], "BaseModel")
        self.assertIsInstance(bmdict["created_at"], str)
        self.assertIsInstance(bmdict["updated_at"], str)
        self.assertEqual(bm.created_at,
                         datetime.datetime.fromisoformat(bmdict["created_at"]))
        self.assertEqual(bm.updated_at,
                         datetime.datetime.fromisoformat(bmdict["updated_at"]))
