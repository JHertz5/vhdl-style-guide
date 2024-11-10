# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent as Rule

lTokens = []
lTokens.append(token.return_statement.label)


class rule_301(Rule):
    """
    This rule checks the indentation of the label.

    **Violation**

    .. code-block:: vhdl

         return_label : return my_value;
         end function;

    **Fix**

    .. code-block:: vhdl

           return_label : return my_value;
         end function;
    """

    def __init__(self):
        super().__init__(lTokens)