
from vsg import rule

import re


class rule_025(rule.rule):
    '''
    Architecture rule 025 checks for valid architecture names.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'architecture', '025')
        self.names = []
        self.solution = 'Architecture name must be one of these: ' + ','.join(self.names)
        self.phase = 7
        self.fixable = False
        self.configuration.append('names')

    def _pre_analyze(self):
        self.lower_names = []
        for sName in self.names:
            self.lower_names.append(sName.lower())

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isArchitectureKeyword:
            lLine = oLine.line.split()
            if lLine[1].lower() not in self.lower_names:
                self.add_violation(iLineNumber)