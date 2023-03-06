def solve(a, b, c):
    root = (-b + (b**2 - 4*a*c) ** 0.5) / (2*a)
    return root

test_table = (
    (1294023, 305001, 1),		
    (1294023, -273801, -9504021),
    (234801, 1294023, 734023),	
    (1294023, -2900202, 230001),	
    (234829, 1294023, -90842),	
    (1294023, 3901203, 234801),	
    (1294023, -2392012, 29092),	
    (398403, 1294023, -2401202),	
    (734023, 1294023, -1294023),	
    (1294023, 432183, 2021),	
    (9504021, -1294023, -273801),
    (1294023, -1294023, 234801),	
    (90842, 1294023, -1294023),	
    (2401202, 1294023, -398403),	
    (1294023, 2392012, 734023),	
)

chk = 0
for i in test_table:
    root = solve(i[0], i[1], i[2])
    chk += abs(root ** 2 * i[0] + root * i[1] + i[2]) < 0.0000001

if chk == len(test_table):
    print("Success!! (", chk, "/", len(test_table),")")
else:
    print("Failed (", chk, "/", len(test_table),")")