from math import erf,sqrt,log

def normal_cdf(x:float)->float:
    return 0.5*(1+erf(x/sqrt(2)))

def btc_probability(log_return:float,variance:float)->float:
    if variance<=0:
        return 0.5
    return normal_cdf(log_return/sqrt(variance))

def conservative(prob:float,uncertainty:float=0.03)->float:
    return max(0.0,min(1.0,prob-uncertainty))
