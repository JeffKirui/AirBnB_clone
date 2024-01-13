#!/usr/bin/python3


""" Module tests/test_models/test_review"""
import models
from models.base_model import BaseModel
from models.review import Review
import os
import unittest


class TestReview(unittest.TestCase):
    """ class TestReview """

    def test_docstring(self):
        """ function test_docstring """
        msj = "Módulo does not has docstring"
        self.assertIsNotNone(models.review.__doc__, msj)
        msj = "Clase does not has docstring"
        self.assertIsNotNone(Review.__doc__, msj)

    def test_executable_file(self):
        """ function test_executable_file """
        is_read_true = os.access("models/review.py", os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access("models/review.py", os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access("models/review.py", os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        """ function test_is_an_instance """
        my_review = Review()
        self.assertIsInstance(my_review, Review)
