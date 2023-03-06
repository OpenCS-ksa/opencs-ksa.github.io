# function that check is leap year
def IS_LEAP_YEAR(year):
    if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
            return 1
    return 0
    

test_table = (
    1893,
    1976,
    2009,
    1912,
    1958,
    1985,
    2011,
    1962,
    2000,
    2002,
    2004,
    1000,
    1953,
    2018,
    1906,
    1979,
    2008,
    1929,
    1982,
    1967,
    2016,
    1904,
    1964,
    1934,
    2000,
    1973,
    1996,
    1917,
    1956,
    2015,
    1943,
    1990,
    1948,
    1975,
    1989,
    1961,
    1902,
    1935,
    1954,
    1919,
    2006,
    1971,
    2017,
    1947,
    1939,
    1968,
    1992,
    1941,
    2003,
    1909
)

chk = 0
for i in test_table:
    chk += isLeapYear(i) == IS_LEAP_YEAR(i)

if chk == len(test_table):
    print("Success!! (", chk, "/", len(test_table),")")
else:
    print("Failed (", chk, "/", len(test_table),")")