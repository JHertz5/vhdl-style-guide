
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.selected_force_assignment.with_keyword)


class rule_500(Rule):
    '''
    This rule checks the **with** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       WITH mux_sel select
         addr <= force "0000" when 0,
                       "0001" when 1,
                       "1111" when others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select
         addr <= force "0000" when 0,
                       "0001" when 1,
                       "1111" when others;
    '''

    def __init__(self):
        Rule.__init__(self, 'selected_force_assignment', '500', lTokens)
        self.groups.append('case::keyword')