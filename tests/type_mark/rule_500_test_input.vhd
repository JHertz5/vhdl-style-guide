
entity FIFO is

  generic (
    G_GEN1 : std_logic;
    G_GEN2 : std_logic_vector(3 downto 0);
    G_GEN3 : integer;
    G_GEN4 : signed(15 downto 0);
    G_GEN5 : unsigned(7 downto 0)
  );
  port (
    I_PORT1 : in integer;
    I_PORT2 : in std_logic;
    I_PORTA : in t_user2;
    I_PORT3 : in std_logic_vector(3 downto 0);
    I_PORT4 : in signed(15 downto 0);
    I_PORT5 : in unsigned(7 downto 0);
    I_PORT6 : in std_ulogic;
    I_PORT7 : in t_user1
  );

end entity FIFO;

architecture rtl of fifo is

  type my_type is range 10 to 100;

  subtype my_subtype   is my_type range 10 to 20;
  subtype my_subtype_t is my_external_type range 10 to 20;
  subtype my_int       is integer range 10 to 100;
  subtype my_nat       is natural range 10 to 100;
  subtype my_pos       is positive range 10 to 100;
  subtype my_char      is character range 'a' downto 'b';

  signal s_my_subtype   : my_external_subtype;
  signal s_my_subtype   : my_subtype;
  signal s_my_subtype_t : my_subtype_t;
  signal s_my_int       : my_int;
  signal s_my_nat       : my_nat;
  signal s_my_pos       : my_pos;
  signal s_my_char      : my_char;
  signal s_my_type_t    : my_type;
  signal s_int          : integer;
  signal s_nat          : natural;
  signal s_pos          : positive;
  signal s_char         : character;

  signal my_sig : std_logic;
  constant my_con : std_logic_vector(3 downto 0);

  procedure my_proc (
    init : in std_logic
  ) is
    variable my_sig : std_logic;
    constant my_con : std_logic_vector(3 downto 0);
  begin
  end procedure;

  component MY_COMP is
    generic (
      G_GEN1 : std_logic;
      G_GEN2 : std_logic_vector(3 downto 0);
      G_GEN3 : integer;
      G_GEN4 : signed(15 downto 0);
      G_GEN5 : unsigned(7 downto 0)
    );
    port (
      I_PORT1 : in integer;
      I_PORT2 : in std_logic;
      I_PORTA : in t_user2;
      I_PORT3 : in std_logic_vector(3 downto 0);
      I_PORT4 : in signed(15 downto 0);
      I_PORT5 : in unsigned(7 downto 0);
      I_PORT6 : in std_ulogic;
      I_PORT7 : in t_user1
    );
  end component;

begin

end architecture rtl;

--====== UPPERCASE below

entity FIFO is

  generic (
    G_GEN1 : STD_LOGIC;
    G_GEN2 : STD_LOGIC_VECTOR(3 downto 0);
    G_GEN3 : INTEGER;
    G_GEN4 : SIGNED(15 downto 0);
    G_GEN5 : UNSIGNED(7 downto 0)
  );
  port (
    I_PORT1 : in INTEGER;
    I_PORT2 : in STD_LOGIC;
    I_PORTA : in T_USER2;
    I_PORT3 : in STD_LOGIC_VECTOR(3 downto 0);
    I_PORT4 : in SIGNED(15 downto 0);
    I_PORT5 : in UNSIGNED(7 downto 0);
    I_PORT6 : in STD_ULOGIC;
    I_PORT7 : in T_USER1
  );

end entity FIFO;

architecture rtl of fifo is

  type MY_TYPE is range 10 to 100;

  subtype MY_SUBTYPE   is MY_TYPE range 10 to 20;
  subtype MY_SUBTYPE_T is MY_EXTERNAL_TYPE range 10 to 20;
  subtype MY_INT       is INTEGER range 10 to 100;
  subtype MY_NAT       is NATURAL range 10 to 100;
  subtype MY_POS       is POSITIVE range 10 to 100;
  subtype MY_CHAR      is CHARACTER range 'a' downto 'b';

  signal S_MY_SUBTYPE   : MY_EXTERNAL_SUBTYPE;
  signal S_MY_SUBTYPE   : MY_SUBTYPE;
  signal S_MY_SUBTYPE_T : MY_SUBTYPE_T;
  signal S_MY_INT       : MY_INT;
  signal S_MY_NAT       : MY_NAT;
  signal S_MY_POS       : MY_POS;
  signal S_MY_CHAR      : MY_CHAR;
  signal S_MY_TYPE_T    : MY_TYPE;
  signal S_INT          : INTEGER;
  signal S_NAT          : NATURAL;
  signal S_POS          : POSITIVE;
  signal S_CHAR         : CHARACTER;

  signal my_sig : STD_LOGIC;
  constant my_con : STD_LOGIC_VECTOR(3 downto 0);

  procedure my_proc (
    init : in STD_LOGIC
  ) is
    variable my_sig : STD_LOGIC;
    constant my_con : STD_LOGIC_VECTOR(3 downto 0);
  begin
  end procedure;

  component MY_COMP is
    generic (
      G_GEN1 : STD_LOGIC;
      G_GEN2 : STD_LOGIC_VECTOR(3 downto 0);
      G_GEN3 : INTEGER;
      G_GEN4 : SIGNED(15 downto 0);
      G_GEN5 : UNSIGNED(7 downto 0)
    );
    port (
      I_PORT1 : in INTEGER;
      I_PORT2 : in STD_LOGIC;
      I_PORTA : in T_USER2;
      I_PORT3 : in STD_LOGIC_VECTOR(3 downto 0);
      I_PORT4 : in SIGNED(15 downto 0);
      I_PORT5 : in UNSIGNED(7 downto 0);
      I_PORT6 : in STD_ULOGIC;
      I_PORT7 : in T_USER1
    );
  end component;

begin

end architecture rtl;
