# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

T = 1.6
ND = 1000
nn = np.arange(0, ND+1, 1)
ts = 0.002
tt = nn*ts  #时间间隔
Ts = 0.1    #连续时间的采样周期
M = int(np.round(Ts/ts))
nns = np.arange(1, ND+1, M)
tts = (nns-1)*ts
ks = np.array([1, 2, 3, 4, 3.9, 4])
tds = np.array([0, 0, 0.1, 0.1, 0, 0.15])
K = len(ks)

x = np.zeros((K, (ND+1)), dtype=complex)

for i in range(K):
    k = ks[i]
    td = tds[i]
    x[i, :] = np.exp(1j*2*np.pi*k*(tt - td)/T)
    if i == 5:
        x[i, :] = np.concatenate((x[i, 301:], x[i-3, 0:301]))
    plt.subplot(K,2,2*i+1)
    plt.plot(tt, np.real(x[i, :]))
    plt.plot((tt[0], tt[-1]), (0,0))
    plt.stem(tts, np.real(x[i, nns]), linefmt='--')

N = int(np.round(T/Ts))

xn = x[:, nns[0:N]-1]
np.set_printoptions(suppress=True, precision=2, floatmode='fixed')
print((xn@xn.conj().transpose())/N)
Xk = np.fft.fft(xn[0:N])
kk = np.arange(0, N, 1)
for i in range(K):
    k = ks[i]
    td = tds[i]
    plt.subplot(K, 2, 2 * i + 2)
    plt.stem(kk, np.abs(Xk[i, :]), linefmt='--')

plt.show()