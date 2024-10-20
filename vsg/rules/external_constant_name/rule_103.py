# -*- coding: utf-8 -*-

from vsg.rules.whitespace_after_token import Rule
from vsg.token import external_constant_name as token


class rule_103(Rule):
    """
    This rule checks for a single space after the colon.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       << constant dut.fifo.wr_en :std_logic >>
       << constant dut.fifo.wr_en :     std_logic >>

    **Fix**

    .. code-block:: vhdl

       << constant dut.fifo.wr_en : std_logic >>
       << constant dut.fifo.wr_en : std_logic >>
    """

    def __init__(self):
        Rule.__init__(self, [token.colon])