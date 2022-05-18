from .cas import OuterTotalisticCA

def GameOfLife(init_state, steps, dev='cpu'):
    """
    Game of Life
    """
    return OuterTotalisticCA(224, init_state, steps, device=dev)