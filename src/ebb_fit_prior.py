#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 21:04:40 2020

@author: uttiya
"""

import numpy as np     
import pandas as pd
from scipy.stats import beta as beta_dist
from scipy.optimize import minimize
from dataclasses import dataclass

import matplotlib.pyplot as plt

#prior = namedtuple('prior', ['alpha','beta'])

@dataclass
class Beta:
    alpha: float
    beta: float
    
    def pdf(self, x):
        return beta_dist.pdf(x, self.alpha, self.beta)
        pass
    
    def cdf(self, x):
        return beta_dist.ppf(x, self.alpha, self.beta)
    
    
    def plot(self, x, n):
        """ plots the prior pdf density over the histogram"""
        x_ax = np.linspace(0,1,1000)
        rv = beta_dist(self.alpha, self.beta)
        p = x/n
        plt.hist(p, density = True)
        plt.plot(x_ax, rv.pdf(x_ax))
        plt.title(f'Beta with {self.alpha} and {self.beta}')
        plt.show()
    
    
    
    
def ebb_fit_prior(x, n, method = 'mm', start = np.nan):
    p = x/n
    if (method == 'mm'):
        mu, sig = np.mean(p), np.var(p)
        a = ((1-mu)/sig - 1/mu)*mu**2
        b = a*(1/mu - 1)
        
        fitted_prior = Beta(a,b)
                
        pass
    elif (method == 'mle'):
        
        # starting value
        if (np.isnan(start)):
            mm_est = ebb_fit_prior(x, n, 'mm')
            start = (mm_est.alpha, mm_est.beta)
            #print(start)
        
        # likelihood function: f(a, b)
        def likelihood(pars):
            f = np.sum(beta_dist.pdf(p, pars[0], pars[1]))
            return -f
        
        # optimization function: over a series of params, optimise likelihood
        outp = minimize(likelihood, x0 = start, method = 'BFGS')
        fitted_prior = Betaa(outp.x[0], outp.x[1])
        
                
        pass
    else:
        return ('wrong method')
    
    return fitted_prior
    
    
    pass 


def augment(prior, data, x, n):
    
    # compute the estimates 
    post_alpha = prior.alpha + x
    post_beta = prior.beta + n - x 
    
    eb_est = (x + prior.alpha)/(n + prior.alpha + prior.beta)
    
    posterior = Beta(post_alpha, post_beta)
    
    # compute the posterior credible intervals 
    post_l = beta_dist.ppf(0.025, posterior.alpha, posterior.beta)
    post_u = beta_dist.ppf(0.975, posterior.alpha, posterior.beta)
    
    # add the column
    new_cols = pd.DataFrame({'eb_est': eb_est, 'cred_lower': post_l, 'cred_upper':post_u})
    aug_df = pd.concat([data, new_cols], axis = 1)
    
    return aug_df

    pass


    
    

if __name__ == '__main__':  
    x = np.random.randint(0,100,100)
    n = 100
    p = x/n
    dt = pd.DataFrame({'H':x, 'AB': n, 'est':p})
        
    est1 = ebb_fit_prior(x,n)
    print(est1)
    #est1.plot(x, n)
    
    new_dt = augment(est1, dt, dt.H, dt.AB)
    print(new_dt.head(10))
    
    #est1.plot()
    # print('=============================')
    # est2 = ebb_fit_prior(x,n,'mle')
    # print(est2)
    # est2.plot(x,n)
    

