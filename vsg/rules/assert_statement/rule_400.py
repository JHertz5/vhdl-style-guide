
from vsg import rule
from vsg import parser
from vsg import violation

from vsg.token import assertion
from vsg.token import assertion_statement
from vsg.token import concurrent_assertion_statement

from vsg.vhdlFile import utils


class rule_400(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    trigger : parser object type
       object type to apply the case check against
    '''

    def __init__(self):
        rule.Rule.__init__(self, name="assert", identifier="400")
        self.solution = 'Align with open parenthesis on previous line.'
        self.alignment = 'report'
        self.configuration.append('alignment')
        self.phase = 4

    def analyze(self, oFile):

        lToi = oFile.get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens([assertion.report_keyword], [assertion.severity_keyword, assertion_statement.semicolon, concurrent_assertion_statement.semicolon], True, False, True)

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            if self.alignment == 'report':
                iSpaces = oFile.get_column_of_token_index(oToi.get_start_index()) + 7
            else:
                iSpaces = (lTokens[0].indent + 1) * self.indentSize

            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, parser.carriage_return):
                    iLine += 1
                    if isinstance(lTokens[iToken + 1], parser.whitespace):
                        if len(lTokens[iToken + 1].get_value()) != iSpaces:
                            sSolution = 'Indent line to column ' + str(iSpaces)
                            oViolation = violation.New(iLine, oToi.extract_tokens(iToken + 1, iToken + 1), sSolution)
                            dAction = {}
                            dAction['action'] = 'adjust'
                            dAction['column'] = iSpaces
                            oViolation.set_action(dAction)
                            self.add_violation(oViolation)
                    elif isinstance(lTokens[iToken + 1], parser.blank_line):
                            continue
                    else:
                            sSolution = 'Indent line to column ' + str(iSpaces)
                            oViolation = violation.New(iLine, oToi.extract_tokens(iToken + 1, iToken + 1), sSolution)
                            dAction = {}
                            dAction['action'] = 'insert'
                            dAction['column'] = iSpaces
                            oViolation.set_action(dAction)
                            self.add_violation(oViolation)
                            

    def fix(self, oFile, dFixOnly=None):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.unique_id)
            self._filter_out_fix_only_violations(dFixOnly)
            for oViolation in self.violations[::-1]:
                self._fix_violation(oViolation)
            oFile.update(self.violations)
            self.clear_violations()

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()

        if dAction['action'] == 'adjust':
            lTokens[0].set_value(' '*dAction['column'])
        else:
            lTokens.insert(0, parser.whitespace(' '*dAction['column']))

        oViolation.set_tokens(lTokens)
