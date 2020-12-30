# -*-coding: utf-8-*-
'''
2. cho trước 2 số y, x (y > x). Có 2 cách thay đổi giá trị của x:
	- tăng gấp đôi x
	- bớt x đi 1 đơn vị
Tìm số bước nhỏ nhất để x = y.
'''
'''
chay tu x: -1 va x2 (chua toi uu)
    x = 7, y = 11
    steps: x->6->12->11 
    x = 5, y = 11
    steps: x->10->9->9->7->6->12->11
'''
# def n_steps(x, y):
#     steps = ""
#     while(x != y):
#         if x > y/2:
#             if x * 2 == (y + 1):
#                 x *= 2
#                 steps += "*"
#             else:
#                 x -= 1
#                 steps += "-"

#         elif x <= y/2:
#             x *= 2
#             steps += "*"
    
#     return len(steps)


'''
chay tu y: +1 va /2
    x = 2, y = 20: 20 -> 10 -> 5 -> 6 -> 3 -> 4 -> 2
'''
def n_steps(x, y):
    steps = 0
    while (y != x):
        if y % 2 != 0:
            y += 1
            steps += 1
        if y / 2 >= x:
            y /= 2
            steps += 1
        elif y / 2 < x:
            y += 1
            steps += 1
    return steps
print(n_steps(2,20))