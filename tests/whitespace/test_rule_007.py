# -*- coding: utf-8 -*-

import os
import unittest

from tests import utils
from vsg import vhdlFile
from vsg.rules import whitespace

sTestDir = os.path.dirname(__file__)

lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir, "rule_007_test_input.vhd"))
lExpected = []
lExpected.append("")
utils.read_file(os.path.join(sTestDir, "rule_007_test_input.fixed.vhd"), lExpected)


class test_whitespace_rule(unittest.TestCase):
    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_007(self):
        oRule = whitespace.rule_007()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "whitespace")
        self.assertEqual(oRule.identifier, "007")
        self.assertEqual(oRule.groups, ["whitespace"])

        lExpected = [6, 6, 6, 14, 14, 14, 22]

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_007(self):
        oRule = whitespace.rule_007()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])
