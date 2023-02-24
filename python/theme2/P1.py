'''
def average(a, b):
    # ADD ADDITIONAL CODE HERE!
    return (a + b) / 2
'''

test_table = [
    [1,5],
    [196, 812],
    [239472398, 982734234],
    [23894091082084, 5823048092384],
    [93284090237, 123789712415],
    [-234, -893270],
    [-19273598347, -237498723985],
    [-829374782234, 923741628482],
    [0, 483729428],
    [83737292, 83737292],
    [0, 0],
    [23478979234, 32987493821],
    [83729374859, -9372628952],
    [-9382729885, -9382728384],
    [1294923828293284940, 8282839230282738],
    [-92923834948239, 28384782982817389478],
    [338383772761833, -912821738472837382],
    [282173743837382919, -3],
    [15, -92837383759869687273],
    [-1, 1],
    [1000000000000000000, 1000000000000000001]
]

chk = 0
for i in test_table:
    chk += average(i[0], i[1]) == (i[0] + i[1]) / 2

if chk == len(test_table):
    print("Success!!")
else:
    print("Failed (", chk, "/", len(test_table),")")