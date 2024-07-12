# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.variable_declaration.assignment_operator)


class rule_102(Rule):
    """
    This rule checks for a single space before the assignment.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       variable size : integer      := 32;
       variable width : integer:= 256;

    **Fix**

    .. code-block:: vhdl

       variable size : integer := 32;
       variable width : integer := 256;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.number_of_spaces = ">=1"
