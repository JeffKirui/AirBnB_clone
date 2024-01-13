#!/usr/bin/python3


""" Module tests/test_models/test_place"""
import models
from models.base_model import BaseModel
from models.place import Place
import os
import unittest


class TestPlace(unittest.TestCase):
    """ class TestPlace """

    def test_docstring(self):
        """ function test_docstring """
        msj = "Módulo does not has docstring"
        self.assertIsNotNone(models.place.__doc__, msj)
        msj = "Clase does not has docstring"
        self.assertIsNotNone(Place.__doc__, msj)

    def test_executable_file(self):
        """ function test_executable_file """
        is_read_true = os.access("models/place.py", os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access("models/place.py", os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access("models/place.py", os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """ function test_is_an_instance """
        my_place = Place()
        self.assertIsInstance(my_place, Place)
