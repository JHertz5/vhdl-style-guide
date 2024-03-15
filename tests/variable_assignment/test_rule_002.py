
import os
import unittest

from vsg.rules import variable_assignment
from vsg import vhdlFile
from tests import utils

sTestDir = os.path.dirname(__file__)

lFile, eError =vhdlFile.utils.read_vhdlfile(os.path.join(sTestDir,'rule_002_test_input.vhd'))

lExpected = []
lExpected.append('')
utils.read_file(os.path.join(sTestDir, 'rule_002_test_input.fixed.vhd'), lExpected)


class test_variable_assignment_rule(unittest.TestCase):

    def setUp(self):
        self.oFile = vhdlFile.vhdlFile(lFile)
        self.assertIsNone(eError)

    def test_rule_002(self):
        oRule = variable_assignment.rule_002()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, 'variable_assignment')
        self.assertEqual(oRule.identifier, '002')

        lExpected = []
        lExpected.extend(range(31,33))
        lExpected.extend(range(34,36))
        lExpected.extend(range(37,39))

        oRule.analyze(self.oFile)
        self.assertEqual(lExpected, utils.extract_violation_lines_from_violation_object(oRule.violations))

    def test_fix_rule_002(self):
        oRule = variable_assignment.rule_002()

        oRule.fix(self.oFile)

        lActual = self.oFile.get_lines()

        self.assertEqual(lExpected, lActual)

        oRule.analyze(self.oFile)
        self.assertEqual(oRule.violations, [])