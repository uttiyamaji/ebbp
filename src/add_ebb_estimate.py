#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 01:37:29 2020

@author: uttiya
"""
import numpy as np
import pandas as pd
from ebb_fit_prior import ebb_fit_prior, augment


def add_ebb_estimate(x, n, data):
    
    # get the estimate and the CIs
    # TO DO: which method to choose? mm or mle?
    est = ebb_fit_prior(x, n)
    
    # augment it with the data
    return augment(est, data, x, n)
    
    pass


if __name__ == '__main__':
    x = np.random.randint(0,100,100)
    n = 100
    p = x/n
    dt = pd.DataFrame({'H':x, 'AB': n, 'est':p})
    
    aug_df = add_ebb_estimate(dt.H, dt.AB, dt)
    print(aug_df.head(10))
    
    
    
    
    