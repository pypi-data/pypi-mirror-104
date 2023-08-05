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
import datetime

import carbon3d
from carbon3d.models.build import Build  # noqa: E501
from carbon3d.rest import ApiException

class TestBuild(unittest.TestCase):
    """Build unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Build
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.build.Build()  # noqa: E501
        if include_optional :
            return Build(
                uuid = '0', 
                packing_group = '0', 
                parts = [
                    {"uuid":"6401c93f-f340-4da2-8784-bddd4065e75c","part_number":"12345","model_uuid":"3cc663e2-c762-4f8f-8997-30d17bc13e8d"}
                    ], 
                attachments = [
                    carbon3d.models.build_attachments.Build_attachments(
                        filename = '0', 
                        uuid = '0', )
                    ], 
                name = '0', 
                revision = '0', 
                status = 'Unreleased'
            )
        else :
            return Build(
                uuid = '0',
                parts = [
                    {"uuid":"6401c93f-f340-4da2-8784-bddd4065e75c","part_number":"12345","model_uuid":"3cc663e2-c762-4f8f-8997-30d17bc13e8d"}
                    ],
        )

    def testBuild(self):
        """Test Build"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
