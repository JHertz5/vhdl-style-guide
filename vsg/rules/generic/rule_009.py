
from vsg.rules import case_rule
from vsg import utils


class rule_009(case_rule):
    '''
    Generic rule 009 checks the "generic" keyword has proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'generic', '009', 'isGenericKeyword', utils.extract_first_keyword)
        self.solution = 'Change generic keyword to ' + self.case + 'case'
