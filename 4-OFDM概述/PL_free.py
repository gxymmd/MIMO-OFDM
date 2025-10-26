# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 11:14:04 2025

@author: 13093
"""

import numpy as np

def PL_free(fc, dist, Gt=1, Gr=1):
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


    PL_F = 20*np.log10((4*np.pi*dist)/(lamda*Gt*Gr))
    
    return PL_F
    
