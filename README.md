# ebbp : Empirical Bayes on the Binomial in Python

It's an unofficial Python implementation of the R package ebbr(Empirical Bayes on the Binomial in R) \

## Usage so far

visit http://varianceexplained.org/r/ebbr-package/ and https://github.com/dgrtwo/ebbr

```python
import ebbp
import numpy as np
import pandas as pd

# random data
x = np.random.randint(0,100,100)
n = 100
p = x/n
dt = pd.DataFrame({'S":x, 'T':n, 'est':p})

# fit the prior over the data using Maximum Likelihood Estimate or Method of Moments 
pr_est = ebbp.ebb_fit_prior(x, n, dt, method = 'mle')

# plot the prior distribution curve over the histogram
pr_est.plot()

# add the shrinkage estimate from the posterior, 95% credible intervals in the dataframe
aug_df = ebbp.augment(pr_est, dt, dt.S, dt.T)
print(aug_df.head(10))

# this previous can be done using 
aug_df = ebbp.add_ebb_estimate(dt.S, dt.T, dt, 'mm')

# if it is required to update the prior only on a subset of the data, then the previous two functions have to be used

```
## Things to add
The routine for fitting the mixture of priors is going to be very useful. It's a bit tricky to implement 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
