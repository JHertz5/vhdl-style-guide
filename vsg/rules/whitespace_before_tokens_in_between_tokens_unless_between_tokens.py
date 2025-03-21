# -*- coding: utf-8 -*-

from vsg import parser, violation
from vsg.rules import utils as rules_utils
from vsg.rules.whitespace_between_tokens import Rule as WhitespaceRule


class Rule(WhitespaceRule):
    """
    Checks for at least a single space before a token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token object types
       reference token to check for a whitespace before

    oStart : token object type
       The beginning of the range

    oEnd : token object type
       The end of the range
    """

    def __init__(self, lTokens, oStart, oEnd, lUnless):
        WhitespaceRule.__init__(self)
        self.lTokens = lTokens
        self.oStart = oStart
        self.oEnd = oEnd
        self.lUnless = lUnless

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_token_and_n_tokens_before_it_in_between_tokens_unless_between_tokens(self.lTokens, 2, self.oStart, self.oEnd, self.lUnless)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if rules_utils.token_is_at_beginning_of_line(lTokens):
                continue
            lReturn.append(extract_toi(oToi))
        return lReturn


def extract_toi(oToi):
    lTokens = oToi.get_tokens()
    if isinstance(lTokens[1], parser.whitespace):
        return oToi
    else:
        return oToi.extract_tokens(1, 2)
