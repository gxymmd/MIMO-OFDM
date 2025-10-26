# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 11:31:06 2025

@author: 13093
"""


import numpy as np
import matplotlib.pyplot as plt

import PL_free
import PL_logdist_or_norm

fc = 1.5e9
d0=100
sigma=3
distance = np.arange(1, 33, 2)**2
Gt = np.array([1, 1, 0.5])
Gr = np.array([1, 0.5, 0.5])
Exp = np.array([2, 3, 6])

y_free = np.zeros((3, len(distance)))
y_logdist = np.zeros((3, len(distance)))
y_lognorm = np.zeros((3, len(distance)))


for k in range(0, 3):
    y_free[k,:] = PL_free.PL_free(fc, distance, Gt[k], Gr[k])
    y_logdist[k, :] = PL_logdist_or_norm.PL_logdist_or_norm(fc, distance, d0, Exp[k])
    y_lognorm[k, :] = PL_logdist_or_norm.PL_logdist_or_norm(fc, distance, d0, Exp[1], sigma)

plt.subplot(3,1,1)
plt.semilogx(distance,y_free[0,:], distance,y_free[1,:], distance,y_free[2,:])
plt.subplot(3,1,2)
plt.semilogx(distance,y_logdist[0,:], distance,y_logdist[1,:], distance,y_logdist[2,:])
plt.subplot(3,1,3)
plt.semilogx(distance,y_lognorm[0,:], distance,y_lognorm[1,:], distance,y_lognorm[2,:])
plt.show()