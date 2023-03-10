#function that check two circle intersected
def CIR(x1, y1, r1, x2, y2, r2):
    if (x1 - x2)**2 + (y1 - y2)**2 <= r1**2 + r2**2:
        return 1
    else:
        return 0

test_table = (   
)

chk = 0
for i in test_table:
    chk += intersection(i[0], i[1], i[2]) == CIR(i[0], i[1], i[2])

if chk == len(test_table):
    print("Success!! (", chk, "/", len(test_table),")")
else:
    print("Failed (", chk, "/", len(test_table),")")