# cython: language_level=3
# cython: boundscheck=False
# cython: nonecheck=False
# cython: wraparound=False
# cython: initializedcheck=False
# cython: cdivision=True

# amalgamation structure that can become a cluster
# Author: Pavel "DRUHG" Artamonov
# License: 3-clause BSD

import numpy as np
cimport numpy as np
import sys

cdef np.double_t EPS = sys.float_info.min


from libc.math cimport fabs, pow

cdef np.double_t merge_means(np.intp_t na, np.double_t meana,
                             np.intp_t nb, np.double_t meanb
                            ):
    # https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance
    # Chan et al.[10] Welford's online algorithm
    cdef np.double_t delta

    # nx = na + nb
    delta = meanb - meana
    delta = meana + delta*nb/(na + nb)
    # use this for big n's
    # mu = (mu*n + mu_2*n_2) / nx
    # m2a = m2a + m2b + delta**2*na*nb/nx
    return delta


cdef class Amalgamation (object):
    # declarations are in pxd file
    # https://cython.readthedocs.io/en/latest/src/userguide/sharing_declarations.html

    def __init__(self, int size = 1, double energy = 0., int clusters = 1):
        self.size = size
        self.energy = energy
        self.clusters = clusters

    # cdef Border _whole_best(self, np.double_t g, Amalgamation other, verbose):
    #     cdef Border brd
    #
    #     brd.dis = pow(g, 1.)
    #     brd.quantity = pow(1.*min(self.size, other.size), 0.5)
    #     brd.measure = pow((1.*self.clusters + other.clusters)/max(self.clusters, other.clusters), +0.25)
    #
    #     brd.limit = brd.dis*brd.quantity*brd.measure*self.clusters
    #     brd.jump = brd.dis*self.size*brd.measure # можно добавить квонтити или пересчитать меру
    #
    #     if verbose and self.size > 1:
    #         print (min(self.size, other.size) > 1, other.size, brd.limit > self.energy, self.size, self.clusters, 'dis', brd.dis, 'lim', brd.limit, self.energy )
    #     return brd

    cdef Border _whole_best(self, np.double_t g, Amalgamation other, verbose):
        cdef Border brd

        brd.dis = pow(g, 1.)
        brd.quantity = self.clusters
        brd.measure = pow(1.*min(self.size, other.size), +0.5)

# есть мера принадлежности
# FAILED druhg/tests/test_druhg.py::test_three_blobs - assert 4 == 3 один из пузырей развалился. Это старый вариант мёрдж мина.
# + synthetic outlier. Выбросы вокруг кластеров!
# если убрать макс, то хамелеон не сработает.
# нет меры принадлежности
# - хамелеон не собрался
# - synthetic outlier. Выбросов нет
#         brd.limit = brd.dis * pow(1.*min(self.size, other.size), +0.5) * pow((1.*self.clusters + other.clusters)/max(self.clusters, other.clusters), +0.25)*self.clusters
#         brd.jump = brd.limit*self.size/self.clusters

# НАИЛУЧШИЕ ИЗ ВАРИАНТОВ ============================================================
# есть мера принадлежности
# -+ ирис получаем 4, а не три кластера assert 0.7909692585742752 >= 0.85
# + хамелеон. половинку надо бить.
# + compound.
# -+ synthetic outlier. нужно разобраться в чём идея теста.
# нет меры принадлежности
# + ирис
# + хамелеон. половинку надо бить.
# +- compound. спряталась сердцевинка
# -+ synthetic outlier. хуже, чем с мерой.
        brd.limit = brd.dis * self.clusters * pow(1.*min(self.size, other.size), 0.5) #* pow((1.*self.clusters + other.clusters)/max(self.clusters, other.clusters), +0.25)
        brd.jump = brd.dis * self.size


# есть мера принадлежности
# - test_iris - assert 0.7909692585742752 >= 0.85
# - хамелеон. центральный кусочек не собрался - состоит из нескольких частей
# + compound
# - synthetic outlier
# нет меры принадлежности
# + хамелеон. половинку отдельно разбивать.
# + compound. спряталась сердцевинка
# - synthetic outlier.
# + test_hdbscan_clusterable_data - assert 7 == 6. На единичку больше?
#         brd.limit = brd.dis * pow(1.*min(self.size, other.size), +0.5) * pow((1.*self.clusters + other.clusters)/max(self.clusters, other.clusters), +0.25) * self.clusters
#         brd.jump = brd.dis * self.size * pow((1.*self.clusters + other.clusters)/max(self.clusters, other.clusters), +0.25)


# есть мера принадлежности
# - test_iris - assert 0.7909692585742752 >= 0.85
# + хамелеон. половинку отдельно разбивать.
# + compound.
# +- synthetic outlier. получилось?
# нет меры принадлежности
# + хамелеон. половинку отдельно разбивать.
# + compound. спряталась сердцевинка
# - synthetic outlier. что я хотел?
# при возврате первой меры test_iris - assert 0.7909692585742752 >= 0.85
#         brd.limit = brd.dis * self.clusters * pow(1.*min(self.size, other.size), +0.5)
#         brd.jump = brd.dis*self.size

# есть мера принадлежности
# квадрат не работает
# всё плохо
# нет меры принадлежности
# всё очень слишком собирается
# +- хамелеон. всё собралось, потом два кусочка, и при разбитии не очень получилось
# + compound. спряталась половина, спряталась сердцевинка
# + synthetic outlier. ято я хотел?
#         brd.limit = brd.dis * self.clusters * pow(1.*self.size, +0.5)
#         brd.jump = brd.limit

# тестики тычинки
# есть мера принадлежности
#         brd.limit = brd.dis *self.clusters * pow(1.*min(self.size, other.size), 2.) # * pow((1.*self.clusters + other.clusters)/max(self.clusters, other.clusters), +0.25)
#         brd.jump = brd.limit/self.clusters *self.size


        if verbose and (self.size > 1 or other.size==1):
            print (min(self.size, other.size) > 1, other.size, brd.limit > self.energy, self.size, self.clusters, 'dis', brd.dis, 'lim', brd.limit, self.energy )
        # print (max(self.size, other.size), min(self.size, other.size), 'whole', 1.*quality*quantity*measure,'=', 1.*self.clusters, quality, quantity, measure)
        return brd

    cdef Border _whole_test(self, np.double_t g, Amalgamation other, verbose):
        cdef Border brd

        brd.dis = pow(g, 1.)
        brd.quantity = 1.*self.clusters
        brd.measure = pow(1.*other.size/self.size, +0.5)

        brd.limit = brd.dis*brd.quantity*brd.measure

        # brd.jump = brd.dis*brd.quantity*self.size*brd.measure
        brd.jump = brd.limit*self.size

        if brd.limit >= self.energy:
            # dis = brd.limit/self.energy
            jump = brd.dis*brd.measure*brd.measure

        if verbose and self.size > 1:
            print (min(self.size, other.size) > 1, other.size, brd.limit > self.energy, self.size, self.clusters, 'dis', brd.dis, 'lim', brd.limit, self.energy )
        # print (max(self.size, other.size), min(self.size, other.size), 'whole', 1.*quality*quantity*measure,'=', 1.*self.clusters, quality, quantity, measure)
        return brd

    cdef Border _whole(self, np.double_t g, Amalgamation other, verbose):
        return self._whole_best(g, other, verbose)
        # return self._whole_test(g, other, verbose)

    cdef np.intp_t limit_to_ought(self, np.double_t g, Amalgamation other):
        # Die Schranke und das Sollen
        # can a new whole overcome its' parts?
        cdef Border brd

        brd = self._whole(g, other, False)
        # print (whole > self.energy + EPS, whole, self.energy + EPS)
        return brd.limit >= self.energy

    cdef Amalgamation merge_amalgamations(self, np.double_t g, Amalgamation other):
        cdef:
            np.intp_t osize, oclusters
            np.double_t oenergy
            Border brd1, brd2
            Amalgamation ret

        ret = self
        if self.size == 1:
            ret = Amalgamation(1, 0., 1)
# ----------------------
        osize, oenergy, oclusters = other.size, other.energy, other.clusters

        brd1 = self._whole(g, other, True)
        brd2 = other._whole(g, self, True)
# ----------------------
        if brd1.limit >= self.energy:
            ret.energy = brd1.jump
            ret.clusters = 1
# ----------------------
        if brd2.limit >= oenergy:
            oenergy = brd2.jump
            oclusters = 1
# ----------------------

        ret._amalgamate(osize, oenergy, oclusters)
        return ret

    cdef void _amalgamate(self, np.intp_t size, np.double_t energy, np.intp_t clusters):
        self.energy += energy
        # self.energy = merge_means(self.clusters, self.energy, clusters, energy)
        self.size += size
        self.clusters += clusters
