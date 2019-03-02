
from vsg import rule

import re


class rule_024(rule.rule):
    '''
    Architecture rule 024 checks for the architecture name in the "end architecture" statement.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'architecture', '024')
        self.solution = 'Add architecture name keyword.'
        self.phase = 1

    def analyze(self, oFile):
        self.dFix['label'] = {}
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword:
                sLabel = oLine.line.split()[1]
            if oLine.isEndArchitecture and not re.match('^\s*end\s+architecture\s+\w+', oLine.line, re.IGNORECASE):
                if re.match('^\s*end\s+architecture', oLine.line, re.IGNORECASE):
                    self.add_violation(iLineNumber)
                    self.dFix['label'][iLineNumber] = sLabel
                elif not re.match('^\s*end\s+\w+', oLine.line, re.IGNORECASE):
                    self.add_violation(iLineNumber)
                    self.dFix['label'][iLineNumber] = sLabel

    def _fix_violations(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if iLineNumber in self.dFix['label']:
                sLine = oLine.line
                oLine.update_line(sLine.replace(';', ' ' + self.dFix['label'][iLineNumber].upper() + ';', 1))
