"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.nina.model.ags_overview_result_inner_payload_data_area import (
    AGSOverviewResultInnerPayloadDataArea,
)
from deutschland.nina.model.ags_overview_result_inner_payload_data_trans_keys import (
    AGSOverviewResultInnerPayloadDataTransKeys,
)

from deutschland import nina

globals()[
    "AGSOverviewResultInnerPayloadDataArea"
] = AGSOverviewResultInnerPayloadDataArea
globals()[
    "AGSOverviewResultInnerPayloadDataTransKeys"
] = AGSOverviewResultInnerPayloadDataTransKeys
from deutschland.nina.model.ags_overview_result_inner_payload_data import (
    AGSOverviewResultInnerPayloadData,
)


class TestAGSOverviewResultInnerPayloadData(unittest.TestCase):
    """AGSOverviewResultInnerPayloadData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAGSOverviewResultInnerPayloadData(self):
        """Test AGSOverviewResultInnerPayloadData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AGSOverviewResultInnerPayloadData()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
