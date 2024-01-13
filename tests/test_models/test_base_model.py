#!/usr/bin/python3


""" Module tests/test_models/test_base_model"""
from models.base_model import BaseModel
import models
import os
import unittest


class TestBase_Model(unittest.TestCase):
    """ class TestBase_Model """

    def test_docstring(self):
        """ function test_docstring """
        msj = "Módulo does not has docstring"
        self.assertIsNotNone(models.base_model.__doc__, msj)
        msj = "Clase does not has docstring"
        self.assertIsNotNone(BaseModel.__doc__, msj)

    def test_executable_file(self):
        """ function test_executable_file """
        is_read_true = os.access("models/base_model.py", os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access("models/base_model.py", os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access("models/base_model.py", os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """ function test_is_an_instance """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_id(self):
        """ function test_id """
        my_model = BaseModel()
        my_model1 = BaseModel()
        self.assertNotEqual(my_model.id, my_model1.id)

    def test_save(self):
        """ function test_save """
        my_model2 = BaseModel()
        first_updated = my_model2.updated_at
        my_model2.save()
        second_updated = my_model2.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict(self):
        """ function test_to_dict """
        my_model3 = BaseModel()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3["__class__"] == "BaseModel":
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == "created_at":
                self.assertIsInstance(value, str)
            if key == "updated_at":
                self.assertIsInstance(value, str)
