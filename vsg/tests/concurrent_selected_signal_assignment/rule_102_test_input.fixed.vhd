architecture rtl of fifo is

begin

  with mux_select select addr <= "0000" when 0,
                                 "0001" when 1,
                                 "1111" when others;

  with mux_select select addr <= "0000" when 0,
                                 "0001" when 1,
                                 "1111" when others;

  with mux_select select (addr) <= "0000" when 0,
                                   "0001" when 1,
                                   "1111" when others;

end architecture rtl;
