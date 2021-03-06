import torch
from .utils import toformat, circular_padding, neighbor_count


def f(x, code):
    r'''code is \sim_n f(n)2^n
    
    The code following is pickup the x-th digit (from back to front) of the code.
    '''
    return int(code & (1 << x) > 0)

def totalistic_update(arr, code, dev='cpu'):
    r'''Apply totalistic update rule on [arr], with rule number [code].
    '''
    arr = arr.to(dev)

    n = neighbor_count(arr, dev=dev)
    
    output = torch.zeros_like(n)
    for i in range(10):
        output[n == i] = f(i, code)
    
    return output.type(arr.type())