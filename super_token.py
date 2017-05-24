#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rstr


class MyToken():
    def generate_token(self):
        return rstr.xeger(r'([A-Za-z0-9]{6,})')