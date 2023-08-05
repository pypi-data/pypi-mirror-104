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
from carbon3d.models.part_orders_response_part_orders import PartOrdersResponsePartOrders  # noqa: E501
from carbon3d.rest import ApiException

class TestPartOrdersResponsePartOrders(unittest.TestCase):
    """PartOrdersResponsePartOrders unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PartOrdersResponsePartOrders
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = carbon3d.models.part_orders_response_part_orders.PartOrdersResponsePartOrders()  # noqa: E501
        if include_optional :
            return PartOrdersResponsePartOrders(
                uuid = '0', 
                status = 'open', 
                part_order_number = '0', 
                printed_parts_count = 56, 
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                flushed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                build_uuids = [
                    '0'
                    ], 
                build_sop_uuid = '0', 
                packing_group = '0'
            )
        else :
            return PartOrdersResponsePartOrders(
        )

    def testPartOrdersResponsePartOrders(self):
        """Test PartOrdersResponsePartOrders"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
