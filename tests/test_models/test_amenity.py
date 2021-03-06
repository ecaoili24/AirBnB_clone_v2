#!/usr/bin/python3
"""test for amenity"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ sets up an instance of an Amenity"""
        cls.amentity = Amenity()
        cls.amenity.name = "TV"

    @classmethod
    def tearDown(self):
        """ tears down an instance of an Amenity"""
        del cls.amenity

    def tearDown(self):
        """ teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8(self):
        """ tests files to pep8 standard"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_diff_id(self):
        """ tests to make sure both instances have different ids"""
        a2 = Amenity()
        self.assertNotEqual(self.a1.id, a2.id)

    def test_is_subclass_Amenity(self):
        """ test if Amenity is subclass of Basemodel"""
        self.assertTrue(issubclass(self.amenity.__class__, Base

    def test_attributes(self):
        """ tests attributes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_str(self):
        """ test to check the string representation """
        self.a1.name = "Theater"
        string = "[{}] ({}) {}".format(self.a1.__class__.__name__,
                                       self.a1.id,
                                       self.a1.__dict__)
        self.assertEqual(str(self.a1), string)

    def test_checking_for_docstring_Amenity(self):
        """checking for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_save_Amenity(self):
        """test if the save works"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """test if dict works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)

if __name__ == "__main__":
    unittest.main()
