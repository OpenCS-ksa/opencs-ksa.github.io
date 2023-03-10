def TestFormula(input):
    pos = input.find("=")
    input = input[:pos] + '=' + input[pos:]
    res = eval(input)
    return res

'''
def ans_get(a, b, c):
    if a + b == c:
        return "+"
    if a - b == c:
        return "-"
    if a * b == c:
        return "*"
    if a / b == c:
        return "/"
    return ""

def ans_formula(a, b, c):
	# Use the two variables below
	oper1 = "" # The First Operator
	oper2 = "" # The Second Operator
    
	# ADD ADDITIONAL CODE HERE!
	oper1 = ans_get(a, b, c)
	oper2 = "="
	if not oper1:
		oper1 = "="
		oper2 = ans_get(b, c, a)
    
	return str(a) + oper1 + str(b) + oper2 + str(c)
    
'''

test_table = (
    (3,6,3),
    (3,3,9),
    (20,4,5),
    (3,20,-17),
    (10,2,5),
    (4,4,0),
    (0,0,0),
    (-5,50,45),
    (8,-2,-4),
    (9,8,17),
    (8,2,4),
    (1,1,2),
    (56,7,8),
    (9,1,9),
    (-8,-2,-10)
)

chk = 0
for i in test_table:
    chk += TestFormula(formula(i[0], i[1], i[2]))

if chk == len(test_table):
    print("Success!! (", chk, "/", len(test_table),")")
else:
    print("Failed (", chk, "/", len(test_table),")")