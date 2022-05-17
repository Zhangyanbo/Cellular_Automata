from .utils import signal_point_init
from .outer_totalistic import outer_totalistic_update
from .totalistic import totalistic_update
import torch


def TotalisticCA(code, init_state, steps, device='cpu'):
    r'''Totalistic CA with rule number [code].

    Reference:
        Packard, Norman H., and Stephen Wolfram. "Two-dimensional cellular automata."
        Journal of Statistical physics 38.5 (1985): 901-946.

    Inputs:
        code: rule number
        init_state: initial state
        steps: number of steps
        device: device to run on
    
    Outputs:
        arr: final state
    '''
    arr = init_state
    for i in range(steps):
        arr = totalistic_update(arr, code)
    return arr

def OuterTotalisticCA(code, init_state, steps, device='cpu'):
    r'''Outer-totalistic CA with rule number [code].

    Reference:
        Packard, Norman H., and Stephen Wolfram. "Two-dimensional cellular automata."
        Journal of Statistical physics 38.5 (1985): 901-946.

    Inputs:
        code: rule number
        init_state: initial state
        steps: number of steps
        device: device to run on
    
    Outputs:
        arr: final state
    '''
    arr = init_state
    for i in range(steps):
        arr = outer_totalistic_update(arr, code)
    return arr