# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.vhdlFile import utils


def set_token_indent(dIndentMap, lTokens):
    lTokenKeys, dIndents = process_indent_map(dIndentMap)
    cParams = parameters()
    cParams.lTokenKeys = lTokenKeys
    cParams.dIndents = dIndents
    cParams.library_name = []
    cParams.dOptions = dIndentMap["indent"]["options"]

    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, parser.whitespace):
            continue

        if isinstance(oToken, parser.blank_line):
            cParams.bLibraryFound = False
            continue

        if isinstance(oToken, parser.carriage_return):
            continue

        sUniqueId = oToken.get_unique_id(sJoin=":")

        iTokenIndent = None

        if sUniqueId in cParams.lTokenKeys:
            token_key = cParams.dIndents[sUniqueId]["token"]
            after_key = cParams.dIndents[sUniqueId]["after"]
            iTokenIndent = update_indent_var(cParams.iIndent, token_key)
            oToken.set_indent(iTokenIndent)
            cParams.iIndent = update_indent_var(cParams.iIndent, after_key)

        if isinstance(oToken, token.context_declaration.end_keyword):
            cParams.bLibraryFound = False
            continue

        if isinstance(oToken, token.library_clause.keyword):
            cParams.bLibraryFound = True
            continue

        if isinstance(oToken, token.logical_name_list.logical_name):
            cParams.library_name.append(oToken.get_lower_value())

        if clear_library_name(oToken):
            cParams.library_name = []

        if isinstance(oToken, token.use_clause.keyword):
            if not cParams.bArchitectureFound:
                sLibraryName = extract_use_clause_library_name(iToken, lTokens)
                if sLibraryName in cParams.library_name:
                    sIndent = cParams.dIndents[sUniqueId]["token_after_library_clause"]
                else:
                    sIndent = cParams.dIndents[sUniqueId]["token_if_no_matching_library_clause"]
                iIndent = update_indent_var(cParams.iIndent, sIndent)
                oToken.set_indent(iIndent)
            else:
                oToken.set_indent(cParams.iIndent)
            continue

        if isinstance(oToken, token.context_reference.keyword):
            if cParams.bLibraryFound:
                oToken.set_indent(cParams.iIndent + 1)
            else:
                oToken.set_indent(cParams.iIndent)
            continue

        if isinstance(oToken, token.architecture_body.architecture_keyword):
            cParams.bLibraryFound = False
            cParams.bArchitectureFound = True
            continue

        if isinstance(oToken, token.architecture_body.semicolon):
            cParams.bArchitectureFound = False
            continue

        if isinstance(oToken, token.entity_declaration.entity_keyword):
            cParams.bLibraryFound = False
            continue

        if isinstance(oToken, token.package_body.package_keyword):
            cParams.bLibraryFound = False
            continue

        if isinstance(oToken, token.package_declaration.package_keyword):
            cParams.bLibraryFound = False
            continue

        ### Comments
        if isinstance(oToken, parser.comment):
            set_indent_of_comment(cParams, iToken, lTokens)
            continue

        ### Pragmas
        if isinstance(oToken, token.pragma.pragma):
            set_indent_of_pragma(cParams, iToken, lTokens)
            continue

        ### Concurrent signal assignment
        if isinstance(oToken, token.concurrent_signal_assignment_statement.label_name):
            cParams.insideConcurrentSignalAssignment = True
            continue

        if isinstance(oToken, token.concurrent_signal_assignment_statement.postponed_keyword):
            cParams.insideConcurrentSignalAssignment = True
            continue

        if isinstance(oToken, token.concurrent_simple_signal_assignment.target):
            cParams.insideConcurrentSignalAssignment = True
            continue

        if isinstance(oToken, token.concurrent_conditional_signal_assignment.target):
            cParams.insideConcurrentSignalAssignment = True
            continue

        if isinstance(oToken, token.concurrent_selected_signal_assignment.with_keyword):
            cParams.insideConcurrentSignalAssignment = True
            continue

        if isinstance(oToken, token.concurrent_simple_signal_assignment.semicolon):
            cParams.insideConcurrentSignalAssignment = False
            continue

        if isinstance(oToken, token.concurrent_conditional_signal_assignment.semicolon):
            cParams.insideConcurrentSignalAssignment = False
            continue

        if isinstance(oToken, token.concurrent_selected_signal_assignment.semicolon):
            cParams.insideConcurrentSignalAssignment = False
            continue

        oToken.set_indent(iTokenIndent)


def update_indent_var(iIndent, update):
    if str(update).startswith("+"):
        return iIndent + int(update)
    if str(update).startswith("-"):
        return iIndent + int(update)
    if update == "current":
        return iIndent
    return update


def process_indent_map(dIndentMap):
    dReturn = {}
    lTopKeys = list(dIndentMap["indent"]["tokens"].keys())
    for sTopKey in lTopKeys:
        lSubKeys = list(dIndentMap["indent"]["tokens"][sTopKey].keys())
        for sSubKey in lSubKeys:
            sUniqueId = sTopKey + ":" + sSubKey
            dReturn[sUniqueId] = dIndentMap["indent"]["tokens"][sTopKey][sSubKey]

    lReturn = list(dReturn.keys())

    return lReturn, dReturn


def is_use_clause_use_keyword_next(iIndex, lTokens):
    iToken = utils.find_next_non_whitespace_token(iIndex, lTokens)
    if isinstance(lTokens[iToken], token.use_clause.keyword):
        return True
    if isinstance(lTokens[iToken], token.context_reference.keyword):
        return True
    return False


def set_indent_of_pragma(cParams, iToken, lTokens):
    oToken = lTokens[iToken]
    set_indent_of_normal_comment(cParams, iToken, lTokens)


def set_indent_of_comment(cParams, iToken, lTokens):
    oToken = lTokens[iToken]
    if cParams.bLibraryFound:
        set_indent_of_use_clause_comment(cParams, iToken, lTokens)
    elif oToken.is_block_comment:
        set_indent_of_block_comment(cParams, iToken, lTokens)
    else:
        set_indent_of_normal_comment(cParams, iToken, lTokens)


def set_indent_of_normal_comment(cParams, iToken, lTokens):
    oToken = lTokens[iToken]
    if cParams.dOptions["comment"]["align_with_end_of_declarative_part"] and next_token_is_end_of_declarative_part(iToken, lTokens):
        oToken.set_indent(cParams.iIndent)
    elif cParams.dOptions["comment"]["align_with_end_of_statement_part"] and next_token_is_end_of_statement_part(iToken, lTokens):
        oToken.set_indent(cParams.iIndent)
    else:
        oToken.set_indent(get_indent_value_of_next_token(iToken, lTokens, cParams))


def set_indent_of_use_clause_comment(cParams, iToken, lTokens):
    oToken = lTokens[iToken]
    if is_use_clause_use_keyword_next(iToken + 1, lTokens):
        oToken.set_indent(cParams.iIndent + 1)
    else:
        oToken.set_indent(cParams.iIndent)


def set_indent_of_block_comment(cParams, iToken, lTokens):
    oToken = lTokens[iToken]
    if oToken.block_comment_indent == 0:
        oToken.set_indent(0)
    else:
        oToken.set_indent(cParams.iIndent)


lEndOfStatementPartTokenNames = [
    "end_keyword",
]


def next_token_is_end_of_statement_part(iToken, lTokens):
    return next_token_is_in_list(iToken, lTokens, lEndOfStatementPartTokenNames)


lEndOfDeclarativePartTokenNames = [
    "begin_keyword",
]


def next_token_is_end_of_declarative_part(iToken, lTokens):
    return next_token_is_in_list(iToken, lTokens, lEndOfDeclarativePartTokenNames)


def next_token_is_in_list(iToken, lTokens, lList):
    iIndex = utils.find_next_non_whitespace_token(iToken + 1, lTokens)
    oNextToken = lTokens[iIndex]

    if oNextToken.sub_token in lList:
        return True

    return False


def get_indent_value_of_next_token(iToken, lTokens, cParams):
    iIndex = utils.find_next_non_whitespace_token(iToken + 1, lTokens)
    sUniqueId = lTokens[iIndex].get_unique_id(sJoin=":")
    if sUniqueId in cParams.lTokenKeys:
        token_key = cParams.dIndents[sUniqueId]["token"]
        iTokenIndent = update_indent_var(cParams.iIndent, token_key)
        return iTokenIndent
    return cParams.iIndent


class parameters:
    def __init__(self):
        self.lTokenKeys = None
        self.dIndents = None
        self.bLibraryFound = False
        self.bArchitectureFound = False
        self.insideConcurrentSignalAssignment = False
        self.dOptions = {}
        self.iIndent = 0


def clear_library_name(oToken):
    if is_primary_unit(oToken) or is_secondary_unit(oToken):
        return True
    return False


def is_primary_unit(oToken):
    if isinstance(oToken, token.entity_declaration.entity_keyword):
        return True
    if isinstance(oToken, token.configuration_declaration.configuration_keyword):
        return True
    if isinstance(oToken, token.package_declaration.package_keyword):
        return True
    if isinstance(oToken, token.package_instantiation_declaration.package_keyword):
        return True
    return False


def is_secondary_unit(oToken):
    if isinstance(oToken, token.architecture_body.architecture_keyword):
        return True
    if isinstance(oToken, token.package_body.package_keyword):
        return True
    return False


def extract_use_clause_library_name(iToken, lTokens):
    for i in range(iToken, len(lTokens)):
        oToken = lTokens[i]
        if isinstance(oToken, token.use_clause.library_name):
            return oToken.get_lower_value()
    return None
