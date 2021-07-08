# https://www.hackerrank.com/challenges/validate-a-roman-number/problem
# Validating Roman Numerals

regex_pattern = r"(M{0,3})(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))