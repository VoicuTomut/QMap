from itertools import permutations
import numpy as np




def cost(rut, w):
    '''

    :param rut:
    :param w:
    :return:
    '''
    dist = 0
    for i in range(0, len(rut) - 1):
        dist = dist + w[rut[i]][rut[i + 1]]
    dist = dist + w[rut[i + 1]][rut[0]]

    return dist


def get_minim_Brut(w):
    '''
    
    :param w:
    :return:
    '''
    opt = permutations(pub_index)
    opt = list(opt)
    mi = cost(opt[0], w)
    solutions = []

    for rut in opt:
        c = cost(rut, w)
        if (mi > c):
            solutions = []
            solutions.append(rut)
            mi = c
        elif (mi == c):
            solutions.append(rut)

    return mi, solutions