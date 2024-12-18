# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.port_map_aspect.port_keyword)


class rule_300(token_indent):
    """
    This rule checks for the proper indentation of the **port** keyword in port maps.

    **Violation**

    .. code-block:: vhdl

       U_FIFO : FIFO
           port map (
           WR_EN    => wr_en,
           RD_EN    => rd_en,
           OVERFLOW => overflow
         );

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
         port map (
           WR_EN    => wr_en,
           RD_EN    => rd_en,
           OVERFLOW => overflow
         );
    """

    def __init__(self):
        super().__init__(lTokens)
