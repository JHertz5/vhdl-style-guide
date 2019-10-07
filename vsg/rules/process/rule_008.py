
from vsg.rules import case_rule
from vsg import utils


class rule_008(case_rule):
    '''
    Process rule 008 checks the "end" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'process', '008', 'isEndProcess', utils.extract_first_keyword)
        self.solution = 'Change end keyword to ' + self.case + 'case'
