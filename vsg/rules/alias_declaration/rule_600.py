
from vsg.rules import token_prefix as Rule

from vsg import token

lTokens = []
lTokens.append(token.alias_declaration.alias_designator)


class rule_600(Rule):
    '''
    This rule checks for valid prefixes on alias designators.

    Default prefix is *a\_*.

    Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

    **Violation**

    .. code-block:: vhdl

       alias header is name;
       alias footer is name;

    **Fix**

    .. code-block:: vhdl

       alias a_header is name;
       alias a_footer is name;
    '''

    def __init__(self):
        Rule.__init__(self, 'alias_declaration', '600', lTokens)
        self.prefixes = ['a_']
        self.solution = 'Alias designators'