# ebbp : Empirical Bayes on the Binomial in Python

I have tried to implement the R package __ebbr__ (Empirical Bayes on the Binomial in R, by David Robinson) in Python. 
Please visit 
* http://varianceexplained.org/r/ebbr-package/ to get the idea about what the package does and
* https://github.com/dgrtwo/ebbr for the R implementation

This was to learn more about how packaging works in Python

### Installation

```bash
pip install ebbp
```
### Usage so far
Fit Beta priors from data, compute shrinkage estimates, credible intervals, add those to the dataset

### TODO

* Mixture of Beta priors 
* Extend to Multinomial-dirichlet models?
* Priors other than Beta, fit using MCMC

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


### License
[MIT](https://choosealicense.com/licenses/mit/)
