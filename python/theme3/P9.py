def SCORE(a, b, c):
    if a == b == c:
        return 10000 + a * 1000
    if a == b:
        return 1000 + a * 100
    if b == c:
        return 1000 + b * 100
    if c == a:
        return 1000 + c * 100
    return __builtins__.max(a, b, c) * 100

test_table = (
    (1,1,1),
    (5,5,5),
    (6,6,2),
    (3,4,3),
    (2,5,5),
    (4,1,1),
    (2,6,2),
    (3,3,5),
    (4,2,1),
    (3,1,6),
    (2,3,5),
    (1,2,6),
    (3,1,6),
    (4,1,2),
    (2,4,3),
    (4,6,2),
    (5,3,2),
    (6,1,2),
    (3,4,5),
    (4,2,6)
)

chk = 0
for i in test_table:
    chk += SCORE(i[0], i[1], i[2]) == score(i[0], i[1], i[2])

if chk == len(test_table):
    print("Success!! (", chk, "/", len(test_table),")")
else:
    print("Failed (", chk, "/", len(test_table),")")