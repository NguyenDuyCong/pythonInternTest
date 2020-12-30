#-*-coding:utf-8-*-
'''
1. cho 1 dãy số 123456789
chèn vào giữa các số 1 phép toán (+, - or none) để ra kết quả 100
yêu cầu: 
- không dùng package itertools
- không dùng 9 vòng for
'''

operators = ['+', '-']

'''
exprs = ["1"]
i = 2: exprs = ["12", "1+2", "1-2"]
i = 3: exprs = ["123", "1+2", "1-2", "1+2+3", "1+2-3", ..., "12-3"]
i = 4: exprs = ["1234", ...]
i = ...
'''
exprs = ["1"]
for i in range(2,10):
    for j in range(len(exprs)):
        for op in operators:
            exprs.append(exprs[j] + op + str(i))
        exprs[j] += str(i)

target_exprs = []
for expr in exprs:
    if eval(expr) == 100:
        target_exprs.append(expr)

for expr in target_exprs:
    print(expr)