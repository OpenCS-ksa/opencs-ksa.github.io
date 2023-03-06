def oddSum(x1, x2, x3, x4, x5):
    return x1 * (x1 % 2) + x2 * (x2 % 2) + x3 * (x3 % 2) + x4 * (x4 % 2) + x5 * (x5 % 2)

def _OS(x1, x2, x3, x4, x5):
    return x1 * (x1 % 2) + x2 * (x2 % 2) + x3 * (x3 % 2) + x4 * (x4 % 2) + x5 * (x5 % 2)

test_table = (
    (7, 24, 11, 18, 13),
    (33, 29, 46, 18, 15),
    (43, 24, 12, 48, 11),
    (49, 37, 26, 20, 5),
    (26, 15, 31, 23, 9),
    (44, 50, 33, 18, 49),
    (17, 13, 15, 47, 9),
    (5, 16, 48, 33, 42),
    (30, 23, 21, 43, 45),
    (35, 27, 23, 19, 25),
    (39, 42, 17, 25, 15),
    (34, 1, 16, 2, 20),
    (21, 12, 7, 28, 30),
    (24, 49, 50, 20, 8),
    (44, 45, 46, 13, 11),
    (14, 30, 11, 38, 39),
    (28, 29, 21, 22, 16),
    (36, 18, 24, 37, 27),
    (23, 4, 22, 12, 44),
    (19, 32, 8, 20, 34),
    (5, 29, 26, 21, 48),
    (48, 33, 9, 20, 50),
    (17, 47, 11, 15, 9),
    (5, 22, 50, 34, 38),
    (6, 22, 24, 36, 5),
    (10, 35, 46, 24, 44),
    (28, 39, 19, 29, 47),
    (43, 41, 33, 25, 42),
    (21, 4, 9, 47, 11),
    (12, 20, 23, 27, 44),
    (33, 20, 45, 23, 14),
    (45, 46, 2, 26, 39),
    (4, 16, 19, 26, 43),
    (23, 22, 7, 38, 21),
    (50, 43, 31, 26, 32),
    (29, 6, 42, 28, 24),
    (34, 28, 5, 33, 13),
    (3, 18, 39, 31, 45),
    (2, 18, 29, 10, 46),
    (47, 24, 20, 9, 2)
)

chk = 0 
for i in test_table:
    chk += oddSum(i[0], i[1], i[2], i[3], i[4]) == _OS(i[0], i[1], i[2], i[3], i[4])

if chk == len(test_table):
    print("Success!! (", chk, "/", len(test_table),")")
else:
    print("Failed (", chk, "/", len(test_table),")")
