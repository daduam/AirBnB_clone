#!/usr/bin/python3
"""Unit tests for base model module"""

import datetime
import os
import unittest
import uuid

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Defines unit tests for BaseModel"""

    def setUp(self):
        """set up tests"""
        FileStorage._FileStorage__file_path = "test.json"
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """tear down tests"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

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

        storage.reload()
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIn(key, storage.all())
        self.assertDictEqual(bm.to_dict(), storage.all()[key].to_dict())

        bm2 = BaseModel()
        key = "{}.{}".format(bm2.__class__.__name__, bm2.id)
        self.assertIn(key, storage.all())

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

    def test_create_base_model_from_dict(self):
        """Test create BaseModel from dict with kwargs"""
        BaseModel(**{})
        BaseModel(None)

        bm = BaseModel()
        bm_kwargs = BaseModel(**bm.to_dict())
        self.assertEqual(bm.id, bm_kwargs.id)
        self.assertEqual(bm.created_at, bm_kwargs.created_at)
        self.assertEqual(bm.updated_at, bm_kwargs.updated_at)
        self.assertIsNot(bm, bm_kwargs)
