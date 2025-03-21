# -*- coding: utf-8 -*-

import unittest

from vsg.rules import port


class test_rule(unittest.TestCase):
    def test_rule_018(self):
        oRule = port.rule_018()
        self.assertTrue(oRule)
        self.assertEqual(oRule.name, "port")
        self.assertEqual(oRule.identifier, "018")
        self.assertTrue(oRule.deprecated)
