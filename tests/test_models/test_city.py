#!/usr/bin/python3


""" Module tests/test_models/test_city"""
import models
from models.base_model import BaseModel
from models.city import City
import os
import unittest


class TestCity(unittest.TestCase):
    """ class TestCity """

    def test_docstring(self):
        """ function test_docstring """
        msj = "Módulo does not has docstring"
        self.assertIsNotNone(models.city.__doc__, msj)
        msj = "Clase does not has docstring"
        self.assertIsNotNone(City.__doc__, msj)

    def test_executable_file(self):
        """ function test_executable_file """
        is_read_true = os.access("models/city.py", os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access("models/city.py", os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access("models/city.py", os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """ function test_is_an_instance """
        my_city = City()
        self.assertIsInstance(my_city, City)
