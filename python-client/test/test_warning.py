"""
    Bundesamt für Bevölkerungsschutz: NINA API

    Erhalten Sie wichtige Warnmeldungen des Bevölkerungsschutzes für Gefahrenlagen wie zum Beispiel Gefahrstoffausbreitung oder Unwetter per Programmierschnittstelle.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.nina.model.warning_info_inner import WarningInfoInner

from deutschland import nina

globals()["WarningInfoInner"] = WarningInfoInner
from deutschland.nina.model.warning import Warning


class TestWarning(unittest.TestCase):
    """Warning unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWarning(self):
        """Test Warning"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Warning()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
