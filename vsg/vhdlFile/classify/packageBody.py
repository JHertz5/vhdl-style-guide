import re


def packageBody(dVars, oLine):

    # Check package body declarations
    if re.match('^\s*package\s+body', oLine.lineLower) and not oLine.insidePackageBody:
        oLine.isPackageBodyKeyword = True
        oLine.insidePackageBody = True
        oLine.indentLevel = 0
        dVars['iCurrentIndentLevel'] = 1
    if oLine.insidePackageBody:
        if not oLine.insideProcess and not oLine.insideCase and not oLine.insideComponent:
            if re.match('^\s*end\s+', oLine.lineLower):
                oLine.isPackageBodyEnd = True
                oLine.indentLevel = 0
                dVars['iCurrentIndentLevel'] = 0
