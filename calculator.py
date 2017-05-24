#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyCalculator():
    def calculate(self, dict_operation):
        """ Check fields and values from input """
        if not self.check_fields_not_empty(dict_operation):
            return {'error': "Please complete all fields"}
        if not self.check_dict_keys(dict_operation):
            return {'error': "Don't try to hack a calculator"}
        if not self.check_numbers(dict_operation):
            return {'error': "Number fields must be filled with numbers ..."}
        if not self.check_operation(dict_operation):
            return {'error': "Don't try to hack a calculator"}
        return self.do_calculate(dict_operation)

    def do_calculate(self, a_dict):
        """ Call operation function depending on the select value """
        if a_dict["operation"] == "add":
            return self.add(a_dict['n1'], a_dict['n2'])
        elif a_dict["operation"] == "subtract":
            return self.subtract(a_dict['n1'], a_dict['n2'])
        elif a_dict["operation"] == "multiply":
            return self.multiply(a_dict['n1'], a_dict['n2'])
        elif a_dict["operation"] == "divide":
            return self.divide(a_dict['n1'], a_dict['n2'])
    
    def add(self, n1, n2):
        return int(n1) + int(n2)
    
    def subtract(self, n1, n2):
        return int(n1) - int(n2)

    def multiply(self, n1, n2):
        return int(n1) * int(n2)

    def divide(self, n1, n2):
        try:
            retour = int(n1) / int(n2)
            return retour
        except ZeroDivisionError:
             return {'error': "Divide by zero"}

    def check_fields_not_empty(self, a_dict):
        """ Check every fields are filled """
        for key, value in a_dict.items():
            if a_dict[key] == '':
                return False
        return True

    def check_dict_keys(self, a_dict):
        """ Check if we have all keys needed in our dict """
        key_list = ['n1', 'n2', 'operation']
        if not all(key in a_dict for key in key_list):
            return False
        return True

    def check_numbers(self, a_dict):
        """ Check number fields can be converted to int """
        try:
            n1 = int(a_dict['n1'])
            n2 = int(a_dict['n2'])
            return True
        except ValueError:
            return False
        
    def check_operation(self, a_dict):
        """ Check the user don't modified the options value """
        if a_dict['operation'] not in ['add', 'subtract', 'multiply', 'divide']:
            return False
        return True
