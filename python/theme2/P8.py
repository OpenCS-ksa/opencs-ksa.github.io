import math

def _RND(n, k):
    n = int(n * 10 ** (k))
    n += 5
    n //= 10
    return float(n / 10 ** (k-1))

test_table = [
    [7.3498, 2],
    [9.2345, 3],
    [12.8567, 1],
    [3.56789, 0],
    [0.987654, 5],
    [6.728, 1],
    [56.234, 0],
    [89.12345, 3],
    [0.4567, 2],
    [7.98765, 1],
    [0.02345, 4],
    [12.678, 0],
    [34.567, 2],
    [45.6789, 1],
    [1.234567, 3],
    [89.456, 0],
    [6.789, 1],
    [0.1234567, 4],
    [12.34567, 0],
    [56.789, 3],
    [0.23456, 1],
    [9.876, 2],
    [34.5678, 4],
    [89.012, 1],
    [7.1234, 3],
    [0.012345, 2],
    [1.2345, 0],
    [3.45678, 3],
    [12.345, 1],
    [5.6789, 2],
    [0.789, 0],
    [8.0123, 1],
    [34.678, 2],
    [56.7891, 3],
    [0.123456, 4],
    [1.23456, 2],
    [7.8912, 0],
    [9.6678, 1],
    [12.3456, 3],
    [34.567, 2],
    [5.678, 1],
    [0.12345, 4],
    [6.7891, 2],
    [9.8765, 3],
    [34.56789, 1],
    [56.7892, 2],
    [0.234567, 3],
    [1.2345, 0],
    [7.89123, 4],
    [9.56789, 2]
]

chk = 0 
for i in test_table:
    chk += round(i[0], i[1]-1) == _RND(i[0], i[1])

if chk == len(test_table):
    print("Success!! (", chk, "/", len(test_table),")")
else:
    print("Failed (", chk, "/", len(test_table),")")
