
from vsg import rule


class Rule(rule.Rule):
    '''
    Class for assigning rules to the alignment group.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.
    '''

    def __init__(self, name, identifier):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.phase = 5
        self.groups.append('alignment')