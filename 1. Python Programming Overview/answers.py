# No.1
# def calculate_years(principal, interest, tax, desired):
#     i = 0
#     if principal >= desired:
#         return 0
#     while True:
#         i+=1
#         accrued_interest = principal*interest
#         principal += accrued_interest*(1-tax)
#         if principal >= desired:
#             return i
# print(calculate_years(1500,0.07,0.6,5000), "years")


# no.2
# string method
# def expandedForm(num):
#     expanded = [str(int(str(num)[i])*10**(len(str(num))-i-1)) for i in range(len(str(num)))]
#     expand = [i for i in expanded if i != "0"]
#     return " + ".join(expand)
# print(expandedForm(70304120))

# numerical method
# def expandedForm(num):
#     length = 0
#     expanded = []
#     while num % 10**length != num:
#         length+=1
#     for i in range(length,0,-1):
#         if len(expanded) == 0:
#             expanded.append(num//10**(i-1)*10**(i-1))
#         else:
#             num -= expanded[length-i-1]
#             expanded.append(num//10**(i-1)*10**(i-1))
#     expand = [str(i) for i in expanded if i != 0]
#     return " + ".join(expand)
# print(expandedForm(70304120))


# no.3

def tower_builder(n_floors, block_size):
    w, h = block_size
    tower = []
    for i in range(n_floors):
        for j in range(h):
            s = ' '*w*(n_floors-i-1)
            s += '*'*(w+(w*i*2))
            tower.append(s)
    return('\n'.join(tower))
print(tower_builder(6,(2,1)))
