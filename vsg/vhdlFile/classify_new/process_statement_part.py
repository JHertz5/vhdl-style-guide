
from vsg.vhdlFile.classify_new import sequential_statement


def detect(iToken, lObjects):
    '''
    process_statement_part ::=
        { sequential_statement }
    '''

    iLast = 0
    iCurrent = iToken
    while iLast != iCurrent:
        iLast = iCurrent
        iCurrent = sequential_statement.detect(iCurrent, lObjects)
    return iCurrent
