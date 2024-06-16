#!/usr/bin/python3
"""
module for testing file storage
"""
import unittest
import json
import os
from models.engine import file_storage
from tests.test_models.test_base_model import BaseModel

FileStorage = file_storage.FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage Class"""

    def setUp(self):
        """Initial configuration for tests"""
        self.file_path = "file.json"
        # Create an empty file if it doesn't exist
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """Cleanup test files"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_a_dictionary(self):
        """Test whether the instance method 'all' returns a valid dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_instance_obj_to_dict_of_objects(self):
        """Test whether the instance method 'new' adds new object"""
        temp_obj = BaseModel()
        self.storage.new(temp_obj)
        key = f"{temp_obj.__class__.__name__}.{temp_obj.id}"
        self.assertIn(key, self.storage.all().keys())

    def test_save_method_saves_objects_to_file(self):
        """Test whether the save method saves objects to file"""
        expected_objects = {}
        for _ in range(4):
            bs_mdl = BaseModel()
            self.storage.new(bs_mdl)
            key = f"{bs_mdl.__class__.__name__}.{bs_mdl.id}"
            expected_objects[key] = bs_mdl.to_dict()

        self.storage.save()

        self.assertTrue(os.path.exists(self.file_path))
        self.assertGreater(os.path.getsize(self.file_path), 0)
        with open(self.file_path, 'r') as f:
            objects = {k: v for k, v in json.load(f).items()}

        self.assertDictEqual(expected_objects, objects)

    def test_reload_method_reloads_saved_objects(self):
        """Test whether the reload method correctly loads objects from file"""
        expected_objects = {}
        for _ in range(4):
            bs_mdl = BaseModel()
            self.storage.new(bs_mdl)
            key = f"{bs_mdl.__class__.__name__}.{bs_mdl.id}"
            expected_objects[key] = bs_mdl.to_dict()

        self.storage.save()
        self.storage.reload()
        saved_objects = self.storage.all()

        saved_objects_dict = {k: v.to_dict() for k, v in saved_objects.items()}
        self.assertEqual(expected_objects, saved_objects_dict)

    def test_reload_method_does_not_do_anything_for_non_existent_file(self):
        """Test whether reload does not do anything if the file does not exist"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        expected_objects = {}
        for _ in range(4):
            bs_mdl = BaseModel()
            self.storage.new(bs_mdl)
            key = f"{bs_mdl.__class__.__name__}.{bs_mdl.id}"
            expected_objects[key] = bs_mdl.to_dict()
        self.storage.reload()
        existing_objects = self.storage.all()

        existing_objects_dict = {k: v.to_dict() for k, v in existing_objects.items()}
        self.assertEqual(expected_objects, existing_objects_dict)

if __name__ == "__main__":
    unittest.main()
