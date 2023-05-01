from itertools import combinations

str_list = input().split()  # apple is a fruit
str_list.sort()
n = int(input()) # 3
#print(str_list)
len_str = list(range(len(str_list)))
#print(len_str)
combination = list(combinations(str_list,n))
#print(*combination)
for i in combination:
    print(*i)
    
    
#a apple fruit
#a apple is
#a fruit is
#apple fruit is