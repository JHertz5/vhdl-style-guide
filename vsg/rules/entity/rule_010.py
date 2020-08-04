
from vsg.rules import case_item_rule
from vsg.token import entity


class rule_010(case_item_rule):
    '''
    Checks the end keyword has proper case.
    '''

    def __init__(self):
        case_item_rule.__init__(self, 'entity', '010', entity.end_keyword)
        self.regionBegin = entity.end_keyword
        self.regionEnd = entity.end_keyword
