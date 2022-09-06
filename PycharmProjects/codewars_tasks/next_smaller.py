# def next_smaller(n):
#     import itertools
#     res, lst_res = '', []
#     for x in itertools.permutations(str(n)):
#         for i in range(len(str(n))):
#             res = res + x[i]
#         lst_res.append(int(res)) if int(res) < n and res[0] != '0' else None
#         res = ''
#     try:
#         return max(lst_res)
#     except ValueError: 
#         return -1

# print(next_smaller(1027))

def swap(string, index1, index2):
    new_string = list(string)
    new_string[index1], new_string[index2] = string[index2], string[index1]
    new_string = sorted(new_string[:index1]) + new_string[index1:]
    return ''.join(new_string)

def smallest(number):
    if list(number) == sorted(number):
        return -1
    rev_num = number[::-1]
    for i, digit in enumerate(rev_num,0):
        if any(num for num in rev_num[:i] if num < digit):
            _, j = max(((num, j) for j, num in enumerate(rev_num[:i]) if int(num) < int(digit)),key = lambda x:(x[0], x[1]))
            swapped_num = swap(rev_num, i, j)
            if not swapped_num.endswith('0'):
                return int(swapped_num[::-1])
    return -1

x = ['29009','21','531','2071','9','111','135','1027','1231111111111111111111111111111111111111111111111111123456789']
for i in x:
    print(smallest(i))