import torch
from .utils import toformat, circular_padding, neighbor_count


def f_outer(a, n, code):
    r'''code is \sim_n f(n)2^n
    
    The code following is pickup the x-th digit (from back to front) of the code.
    '''
    return int(code & (1 << (2 * n + a)) > 0)

def outer_totalistic_update(arr, code, dev='cpu'):
    r'''Apply outer-totalistic update rule on [arr], with rule number [code].
    '''
    arr = arr.to(dev)

    n = neighbor_count(arr, dev=dev) - arr
    output = torch.zeros_like(n).long()
    for i in range(9):
        output[(n == i) * (arr == 0)] = f_outer(0, i, code)
        output[(n == i) * (arr == 1)] = f_outer(1, i, code)
        
    return output.type(arr.type())