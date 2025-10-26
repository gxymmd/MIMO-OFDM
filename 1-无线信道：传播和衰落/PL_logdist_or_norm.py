# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 11:14:04 2025

@author: 13093
"""

import numpy as np

def PL_logdist_or_norm(fc, d, d0, n, sigma=0):
    """
    

    Parameters
    ----------
    fc : TYPE
        载波频率.
    dist : TYPE
        距离.
    Gt : TYPE, optional
        发射机功率. The default is 1.
    Gr : TYPE, optional
        接收机功率. The default is 1.

    Returns
    -------
    PL_F : TYPE
        路径损耗值DB.

    """
    
    lamda=3e8/fc


    PL = -20*np.log10(lamda/(4*np.pi*d0)) + 10*n*np.log10(d/d0)

    PL = PL + sigma*np.random.randn(len(d))
    return PL
    
