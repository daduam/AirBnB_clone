#!/usr/bin/python3
"""Unit tests for file storage module"""

import os
import unittest

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Defines unit tests for FileStorage"""

    def setUp(self):
        """set up tests"""
        FileStorage._FileStorage__file_path = "test.json"
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """tear down tests"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test all public instance method"""
        fstorage = FileStorage()
        result = fstorage.all()
        self.assertDictEqual(result, FileStorage._FileStorage__objects)

    def test_new(self):
        """Test new public instance method"""
        fstorage = FileStorage()
        bm = BaseModel()
        fstorage.new(bm)
        all_objs = fstorage.all()

        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIn(key, all_objs)
        self.assertIs(bm, all_objs[key])

    def test_save(self):
        """Test save public instance method"""
        fstorage = FileStorage()
        bm = BaseModel()
        fstorage.new(bm)

        objs_before = fstorage.all()
        fstorage.save()
        fstorage.reload()
        objs_after = fstorage.all()

        for key in objs_before:
            self.assertDictEqual(objs_before[key].to_dict(),
                                 objs_after[key].to_dict())

    def test_reload(self):
        """Test reload public instace method"""
        fstorage = FileStorage()
        bm = BaseModel()
        fstorage.new(bm)

        fstorage.save()
        objs_before = fstorage.all()
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        fstorage.reload()
        objs_after = fstorage.all()

        self.assertDictEqual(objs_before, objs_after)
        self.assertIs(objs_before, objs_after)

    def test_storage(self):
        """Test global storage object"""
        self.assertIsInstance(storage, FileStorage)
