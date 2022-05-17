from .cas import OuterTotalisticCA

def GameOfLife(init_state, steps):
    """
    Game of Life
    """
    return OuterTotalisticCA(224, init_state, steps)