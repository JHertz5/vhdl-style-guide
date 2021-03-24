
from vsg.vhdlFile.extract import utils
from vsg.vhdlFile.extract import tokens


def get_line_which_includes_tokens(lTokens, lAllTokens, oTokenMap):

    lReturn = []

    lTokenIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)

    for iIndex in lTokenIndexes:
        iStart = oTokenMap.get_index_of_carriage_return_before_index(iIndex) + 1
        iEnd = oTokenMap.get_index_of_carriage_return_after_index(iIndex)
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        lTemp = lAllTokens[iStart:iEnd]
        lReturn.append(tokens.New(iStart, iLine, lTemp))

    return lReturn
