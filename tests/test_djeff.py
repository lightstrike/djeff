#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_djeff
----------------------------------

Tests for `djeff` module.
"""

import unittest

from djeff import djeff


class TestDjeff(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_djeffify_string_first_letter(self):
        test_string_1 = 'Just a few things to test here for the djeff project for django.'
        expected_out_1 = 'dJust a few things to test here for the djeff project for django.'

        out_1 = djeff.djeffify_string(test_string_1)

        assert(out_1 == expected_out_1)

    def test_001_djeffify_string_newlines(self):
        test_string = ('Start a new string\n'
                       'Jeff all of the things.')
        expected_out = ('Start a new string\n'
                        'dJeff all of the things.')

        out = djeff.djeffify_string(test_string)

        assert(out == expected_out)

    def test_001_djeffify_string_spaces_and_case_insensitive(self):
        test_string = 'We need to test words starting with j, J.'
        expected_out = 'We need to test words starting with dj, dJ.'

        out = djeff.djeffify_string(test_string)

        assert(out == expected_out)

    def test_002_instantiate_parser(self):
        djeff.DjeffParser()

    def test_003_reconstruct_attrs(self):
        test_list = [('attr1', 'val1'), ('attr2', 'val2')]
        expected_out = 'attr1=val1 attr2=val2'

        out = djeff.reconstruct_attrs(test_list)

        assert (out == expected_out)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
