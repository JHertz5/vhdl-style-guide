# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case

lTokens = []
lTokens.append(token.delay_mechanism.reject_keyword)


class rule_502(token_case):
    """
    This rule checks the **reject** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       a <= REJECT 2ns inertial 1 after 10 ns;

    **Fix**

    .. code-block:: vhdl

       a <= reject 2ns inertial 1 after 10 ns;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::keyword")
