import scipy.stats as stats
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

n_sample = 1000

#consider it as given
mean_sampling_distribution = np.mean(df["CreditScore"])

#consider it as given
std_sampling_distribution = np.std(df["CreditScore"])/np.sqrt(n_sample)

#any value related to the problem
x_target_hypothesis = 651
z_score =  (x_target_hypothesis-mean_sampling_distribution)/std_sampling_distribution

#probability to be on the left/right side of the curve
p_inferior_x_crit = stats.norm.cdf(z_score)
p_superior_x_crit = 1- p_inferior_x_crit
print(p_inferior_x_crit)
print(p_superior_x_crit)
