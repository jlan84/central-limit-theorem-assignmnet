import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

def graph_hist(ax, data):
    ax.hist(data, bins=5)

if __name__ == "__main__":
    #1
    google_txt = np.loadtxt('../data/lunch_hour.txt')
    mean_lunch = np.mean(google_txt)
    
    #2 According to the central limit theorem, any sample mean of a sufficiently
    # large sample is normally distributed

    #3 
    std_err = np.std(google_txt)/np.sqrt(len(google_txt))
    dist_sample_mean_minus_pop_mean = stats.norm(loc=0, scale=std_err)
    
    alpha = dist_sample_mean_minus_pop_mean.ppf(0.025)
    
    print(f"The 95% confidence interval falls between {mean_lunch+alpha:.4f}\
 and {mean_lunch-alpha:.4f}.")

    """
    #4 If we ran this survey of employee lunches 100 times and computed the CI
    eadh time we would expect that 95 of those 100 CI would contain the true
    population mean

    #5 If the sample size were smaller then the standard error would be larger
    and therefore the 95% CI interval would be larger.  But the theory still
    holds true, but there would be more uncertainty.  

    