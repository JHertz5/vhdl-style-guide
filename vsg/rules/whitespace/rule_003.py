# -*- coding: utf-8 -*-

from vsg import parser
from vsg.rules import remove_spaces_before_token_rule


class rule_003(remove_spaces_before_token_rule):
    """
    This rule checks for spaces before semicolons.

    **Violation**

    .. code-block:: vhdl

       wr_en : in    std_logic      ;

    **Fix**

    .. code-block:: vhdl

       wr_en : in    std_logic;
    """

    def __init__(self):
        super().__init__(parser.semicolon)
        self.solution = "Remove spaces before semicolon."
        self.configuration_documentation_link = None
