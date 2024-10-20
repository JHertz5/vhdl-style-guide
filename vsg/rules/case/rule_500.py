# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens as Rule

lTokens = []
lTokens.append(token.choice.others_keyword)

oStartToken = token.case_statement_alternative.when_keyword

oEndToken = token.case_statement_alternative.assignment


class rule_500(Rule):
    """
    This rule checks the *others* keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       when OTHERS =>

    **Fix**

    .. code-block:: vhdl

       when others =>
    """

    def __init__(self):
        super().__init__(lTokens, oStartToken, oEndToken)
        self.groups.append("case::keyword")
