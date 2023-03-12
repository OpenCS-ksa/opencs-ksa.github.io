test_table = (
    (1,2),
    (-1,-2),
    (1,-2),
    (0,10),
    (0,-10),
    (1,1),
    (-1,-1),
    (-5,0),
    (5,0),
    (100,50),
    (50,100),
    (999,1000),
    (1000,999),
    (500000,500001),
    (-500000,-500001),
    (-500000,500001),
    (2147483647,-2147483648),
    (-2147483648,2147483647),
    (123456789,987654321),
    (-123456789,-987654321),
    (-123456789,987654321),
    (123456789,-987654321),
    (100000000,99999999),
    (99999999,100000000),
    (999,-1000),
    (-999,1000),
    (123,456),
    (-123,-456),
    (789,-123),
    (-789,123),
    (9999,10000),
    (10000,9999),
    (42,-42),
    (-42,42),
    (13,42),
    (-13,-42),
    (0,0),
    (100000000,100000000),
    (-100000000,-100000000),
    (-100000000,100000000),
    (100000000,-100000000),
    (100,-100),
    (-100,100),
    (1,-1),
    (-1,1),
    (2,2),
    (-2,-2),
    (5,-5),
    (-5,5),
    (123456789,123456788)
)

chk = 0
for i in test_table:
    chk += min(i[0], i[1]) == __builtins__.min(i[0],i[1])

if chk == len(test_table):
    print("Success!! (", chk, "/", len(test_table),")")
else:
    print("Failed (", chk, "/", len(test_table),")")