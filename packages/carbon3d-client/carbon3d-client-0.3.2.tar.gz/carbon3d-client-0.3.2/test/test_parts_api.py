# coding: utf-8

"""
    Carbon DLS API

    Welcome to the Carbon DLS API docs!  You can find all relevant documentation here: https://github.com/carbon3d/carbon3d-api   # noqa: E501

    The version of the OpenAPI document: 0.3.2
    Contact: api-list@carbon3d.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import carbon3d
from carbon3d.api.parts_api import PartsApi  # noqa: E501
from carbon3d.rest import ApiException


class TestPartsApi(unittest.TestCase):
    """PartsApi unit test stubs"""

    def setUp(self):
        self.api = carbon3d.api.parts_api.PartsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_part(self):
        """Test case for create_part

        Create a Part  # noqa: E501
        """
        pass

    def test_get_part(self):
        """Test case for get_part

        Fetch a Part  # noqa: E501
        """
        pass

    def test_get_parts(self):
        """Test case for get_parts

        Fetch parts  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
