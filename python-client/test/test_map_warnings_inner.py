"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.nina.model.map_warnings_inner_i18n_title import (
    MapWarningsInnerI18nTitle,
)

from deutschland import nina

globals()["MapWarningsInnerI18nTitle"] = MapWarningsInnerI18nTitle
from deutschland.nina.model.map_warnings_inner import MapWarningsInner


class TestMapWarningsInner(unittest.TestCase):
    """MapWarningsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMapWarningsInner(self):
        """Test MapWarningsInner"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MapWarningsInner()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
