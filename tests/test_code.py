#!/usr/bin/env python
# -*- coding: utf-8 -*

import unittest
import os, sys
sys.path.insert(0, os.path.abspath(".."))
from super_token import MyToken
from calculator import MyCalculator

class TestToken(unittest.TestCase):
    """Test token generation"""
    def test_generate_token(self):
        """ Create 100 token and verify for each of them if they correspond to the regExp """
        tokens = []
        not_required_chars = [u'&',u'é',u'\"',u'\'',u'(',u'-',u'è',u'_',u'ç',u'à',u')',u'=',u'^',u'$',u'ù',u',',
                              u';',u':',u'!',u'¨',u'£',u'€',u'%',u'?',u'.',u'/',u'§',u'~',u'#',u'{',u'[',u'|',u'`',
                              u'\\',u'@',u']',u'}',u'°',u'+',u'-',u'*']
        for i in range(0,100):
            tokens.append(MyToken().generate_token())
        for token in tokens:
            self.assertGreaterEqual(len(token), 6)
            for char in token:
                self.assertNotIn(char, not_required_chars)

class TestCalculator(unittest.TestCase):
    """Test the calculator behavior"""
    def test_check_fields_is_empty(self):
        aDict = {"n1": '', "n2": '', "operation": ''}
        self.assertFalse(MyCalculator().check_fields_not_empty(aDict))

    def test_check_fields_not_empty(self):
        aDict = {"n1": '1', "n2": '2', "operation": 'trololo'}
        self.assertTrue(MyCalculator().check_fields_not_empty(aDict))

    def test_check_dict_keys_false(self):
        aDict = {"n1": '1', "n2": '2'}
        self.assertFalse(MyCalculator().check_dict_keys(aDict))

    def test_check_dict_keys_true(self):
        aDict = {"n1": '1', "n2": '2', "operation": "trololo"}
        self.assertTrue(MyCalculator().check_dict_keys(aDict))

    def test_check_numbers_false(self):
        aDict = {"n1": 'un', "n2": 'deux', "operation": "add"}
        self.assertFalse(MyCalculator().check_numbers(aDict))

    def test_check_numbers_true(self):
        aDict = {"n1": '1', "n2": '2', "operation": "add"}
        self.assertTrue(MyCalculator().check_numbers(aDict))

    def test_check_operation_false(self):
        aDict = {"n1": '1', "n2": '2', "operation": "trololo"}
        self.assertFalse(MyCalculator().check_operation(aDict))

    def test_check_operation_true(self):
        aDict = {"n1": '1', "n2": '2', "operation": "subtract"}
        self.assertTrue(MyCalculator().check_operation(aDict))

    def test_add(self):
        self.assertEqual(MyCalculator().add('-1','2'), 1)

    def test_subtract(self):
        self.assertEqual(MyCalculator().subtract('-1','2'), -3)
    
    def test_multiply(self):
        self.assertEqual(MyCalculator().multiply('-1','2'), -2)
    
    def test_divide(self):
        self.assertEqual(MyCalculator().divide('-2','1'), -2)
    
    def test_divide_by_zero(self): 
        self.assertEqual(MyCalculator().divide('-1','0'), {'error': "Divide by zero"})

if __name__ == '__main__':
    unittest.main()