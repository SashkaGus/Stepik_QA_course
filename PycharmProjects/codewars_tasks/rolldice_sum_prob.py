import itertools
def rolldice_sum_prob(a:int, b:int) -> float:
    res_lst, comm_lst, n, = [],[], 0
    for res_lst in list(itertools.product(range(1,7),repeat=b)):
        if sum(res_lst) == a:
            comm_lst.append(res_lst) 
    res = len(comm_lst)/(6 ** b)
    return 0 if res == 0.0 else res

print(rolldice_sum_prob(22, 5))