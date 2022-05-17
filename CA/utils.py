import torch


def signal_point_init(r):
    r'''return a (2r+1) x (2r+1) matrix, where, only the center point is 1,
    and the rest is 0.
    '''
    r = int(r)
    x = torch.zeros(2*r+1, 2*r+1)
    x[r, r] = 1
    return x.long()

def random_init(size):
    r'''Return a random matrix of size [size].
    '''
    return torch.randint(0, 2, (size, size)).long()

def toformat(arr):
    return arr.squeeze().unsqueeze(0).unsqueeze(0)

def circular_padding(arr):
    return torch.nn.functional.pad(arr, [1, 1, 1, 1], mode='circular')

def neighbor_count(arr):
    r'''Count the total neighbor of arr at each point.
    Input: arr
    Ouput: neighbor count
    '''
    arr = circular_padding(toformat(arr))
    weight = torch.ones(1, 1, 3, 3).long() # running at long type to avoid error
    return torch.nn.functional.conv2d(arr, weight, stride=1)[0, 0]