# -*- coding: utf-8 -*-

from .token_indent import token_indent
from .token_indent_between_tokens import token_indent_between_tokens
from .token_indent_between_tokens_unless_between_tokens import token_indent_between_tokens_unless_between_tokens
from .token_indent_unless_between_tokens import token_indent_unless_between_tokens
from .remove_spaces_before_token_rule import remove_spaces_before_token_rule
from .move_token import move_token
from .move_token_next_to_another_token import move_token_next_to_another_token
from .move_token_next_to_another_token_if_it_exists_between_tokens import move_token_next_to_another_token_if_it_exists_between_tokens
from .move_token_left_to_next_non_whitespace_token import move_token_left_to_next_non_whitespace_token
from .move_token_right_to_next_non_whitespace_token import move_token_right_to_next_non_whitespace_token
from .previous_line import previous_line
from .blank_line_above_line_starting_with_token import blank_line_above_line_starting_with_token

from .line_length import line_length
from .file_length import file_length
from .token_case import token_case
from .token_case_with_prefix_suffix import token_case_with_prefix_suffix
from .token_case_in_range_bounded_by_tokens import token_case_in_range_bounded_by_tokens
from .token_case_in_range_bounded_by_tokens_unless_between_tokens import token_case_in_range_bounded_by_tokens_unless_between_tokens
from .token_case_in_range_bounded_by_tokens_with_prefix_suffix import token_case_in_range_bounded_by_tokens_with_prefix_suffix
from .blank_line_below_line_ending_with_token import blank_line_below_line_ending_with_token
from .blank_line_below_line_ending_with_several_possible_tokens import blank_line_below_line_ending_with_several_possible_tokens
from .insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token import (
    insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token,
)
from .insert_token_left_of_token_if_it_does_not_exist_between_tokens import insert_token_left_of_token_if_it_does_not_exist_between_tokens
from .insert_token_right_of_token_if_it_does_not_exist_between_tokens_using_value_from_token import (
    insert_token_right_of_token_if_it_does_not_exist_between_tokens_using_value_from_token,
)
from .insert_token_next_to_token_if_it_does_not_exist_between_tokens_using_value_from_token import (
    insert_token_next_to_token_if_it_does_not_exist_between_tokens_using_value_from_token,
)
from .is_token_value_one_of import is_token_value_one_of
from .align_tokens_in_region_between_tokens import align_tokens_in_region_between_tokens
from .align_tokens_in_region_between_tokens_unless_between_tokens import align_tokens_in_region_between_tokens_unless_between_tokens
from .align_tokens_in_region_between_tokens_when_between_tokens_unless_between_tokens import (
    align_tokens_in_region_between_tokens_when_between_tokens_unless_between_tokens,
)
from .align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens import align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens
from .align_left_token_with_right_token_if_right_token_starts_a_line import align_left_token_with_right_token_if_right_token_starts_a_line
from .remove_tokens import remove_tokens
from .remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace import remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace
from .insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment
from .insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens import (
    insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens,
)
from .insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens_unless_between_tokens import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens_unless_between_tokens 
from .align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token import (
    align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token,
)

from .align_consecutive_lines_after_line_starting_with_token_and_stopping_with_token import (
    align_consecutive_lines_after_line_starting_with_token_and_stopping_with_token,
)
from .remove_blank_lines_above_line_starting_with_token import remove_blank_lines_above_line_starting_with_token
from .blank_lines_between_token_pairs import blank_lines_between_token_pairs
from .n_spaces_before_and_after_tokens import n_spaces_before_and_after_tokens
from .spaces_before_and_after_tokens_when_bounded_by_tokens import spaces_before_and_after_tokens_when_bounded_by_tokens
from .consistent_token_case import consistent_token_case
from .token_prefix import token_prefix
from .token_prefix_between_tokens import token_prefix_between_tokens
from .token_prefix_between_tokens_unless_between_tokens import token_prefix_between_tokens_unless_between_tokens
from .token_suffix import token_suffix
from .token_suffix_between_tokens import token_suffix_between_tokens
from .token_suffix_between_tokens_unless_between_tokens import token_suffix_between_tokens_unless_between_tokens
from .split_line_at_token import split_line_at_token
from .split_line_at_token_when_between_tokens import split_line_at_token_when_between_tokens
from .split_line_at_token_when_between_tokens_unless_token_is_found import split_line_at_token_when_between_tokens_unless_token_is_found
from .insert_token_right_of_token_if_it_does_not_exist_before_token import insert_token_right_of_token_if_it_does_not_exist_before_token
from .insert_tokens_right_of_token_if_it_does_not_exist_before_token import insert_tokens_right_of_token_if_it_does_not_exist_before_token
from .insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token import insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token
from .remove_excessive_blank_lines_below_line_ending_with_token import remove_excessive_blank_lines_below_line_ending_with_token
from .remove_excessive_blank_lines_above_line_starting_with_token import remove_excessive_blank_lines_above_line_starting_with_token
from .formal_part_in_association_element_between_tokens import formal_part_in_association_element_between_tokens
from .move_token_sequences_left_of_token import move_token_sequences_left_of_token
from .remove_lines_starting_with_token_between_token_pairs import remove_lines_starting_with_token_between_token_pairs
from .token_case_subtype_indication import token_case_subtype_indication
from .separate_multiple_signal_identifiers_into_individual_statements import separate_multiple_signal_identifiers_into_individual_statements
from .remove_carriage_returns_between_token_pairs import remove_carriage_returns_between_token_pairs
from .split_line_at_token_if_on_same_line_as_token_if_token_pair_are_not_on_the_same_line import (
    split_line_at_token_if_on_same_line_as_token_if_token_pair_are_not_on_the_same_line,
)
from .remove_comments_from_end_of_lines_bounded_by_tokens import remove_comments_from_end_of_lines_bounded_by_tokens
from .token_case_formal_part_of_association_element_in_map_between_tokens import token_case_formal_part_of_association_element_in_map_between_tokens
from .token_case_n_token_after_tokens_between_tokens import token_case_n_token_after_tokens_between_tokens
from .token_case_n_token_after_tokens_between_tokens_unless_between_tokens import token_case_n_token_after_tokens_between_tokens_unless_between_tokens
from .existence_of_tokens_which_should_not_occur import existence_of_tokens_which_should_not_occur
from .multiline_alignment_between_tokens import multiline_alignment_between_tokens
from .multiline_structure import multiline_structure
from .multiline_simple_structure import multiline_simple_structure
from .multiline_array_alignment import multiline_array_alignment
from .multiline_constraint_structure import multiline_constraint_structure
from .multiline_procedure_call_structure import multiline_procedure_call_structure
from .multiline_conditional_alignment import multiline_conditional_alignment
from .multiline_subprogram_specification_structure import multiline_subprogram_specification_structure
from .remove_carriage_return_after_token import remove_carriage_return_after_token
from .move_token_to_the_right_of_several_possible_tokens_if_it_exists_between_tokens import (
    move_token_to_the_right_of_several_possible_tokens_if_it_exists_between_tokens,
)
from .number_of_lines_between_tokens import number_of_lines_between_tokens
from .token_does_not_exist_before_token import Rule as token_does_not_exist_before_token

from .experiment import Rule as experiment

from vsg.rules import alias_declaration
from vsg.rules import after
from vsg.rules import aggregate
from vsg.rules import architecture
from vsg.rules import assert_statement
from vsg.rules import attribute
from vsg.rules import attribute_declaration
from vsg.rules import attribute_specification
from vsg.rules import bit_string_literal
from vsg.rules import block
from vsg.rules import block_comment
from vsg.rules import case
from vsg.rules import case_generate_alternative
from vsg.rules import case_generate_statement
from vsg.rules import comment
from vsg.rules import component
from vsg.rules import concurrent
from vsg.rules import conditional_expressions
from vsg.rules import conditional_waveforms
from vsg.rules import constant
from vsg.rules import context
from vsg.rules import context_ref
from vsg.rules import declarative_part
from vsg.rules import element_association
from vsg.rules import entity
from vsg.rules import entity_specification
from vsg.rules import exit_statement
from vsg.rules import exponent
from vsg.rules import external_signal_name
from vsg.rules import external_constant_name
from vsg.rules import external_variable_name
from vsg.rules import file_statement
from vsg.rules import for_loop
from vsg.rules import for_generate_statement
from vsg.rules import function
from vsg.rules import generate
from vsg.rules import generic
from vsg.rules import generic_map
from vsg.rules import ieee
from vsg.rules import if_statement
from vsg.rules import if_generate_statement
from vsg.rules import instantiation
from vsg.rules import iteration_scheme
from vsg.rules import length
from vsg.rules import library
from vsg.rules import logical_operator
from vsg.rules import loop_statement
from vsg.rules import next_statement
from vsg.rules import null_statement
from vsg.rules import package
from vsg.rules import package_body
from vsg.rules import port
from vsg.rules import port_map
from vsg.rules import pragma
from vsg.rules import procedure
from vsg.rules import procedure_call
from vsg.rules import process
from vsg.rules import protected_type
from vsg.rules import protected_type_body
from vsg.rules import ranges
from vsg.rules import record_type_definition
from vsg.rules import report_statement
from vsg.rules import reserved
from vsg.rules import return_statement
from vsg.rules import selected_assignment
from vsg.rules import sequential
from vsg.rules import signal
from vsg.rules import source_file
from vsg.rules import subprogram_body
from vsg.rules import subtype
from vsg.rules import type_definition
from vsg.rules import use_clause
from vsg.rules import variable
from vsg.rules import variable_assignment
from vsg.rules import wait
from vsg.rules import when
from vsg.rules import while_loop
from vsg.rules import whitespace
from vsg.rules import with_statement
