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

#probability/ p_value to be on the left/right side of the curve
p_inferior_x_crit = stats.norm.cdf(z_score)
p_superior_x_crit = 1- p_inferior_x_crit
print(p_inferior_x_crit)
print(p_superior_x_crit)

if p_inferior_x_crit <= 0.05:
  print("Probability of x_crit to occur is <5%: unlikely based on conventional confidence level, 95%")

  #Reverse method:
 confidence_level = 0.95 
 #alpha, aka p_critical
 alpha = 1- confidence_level
 
  #if the z_score_hypothesis is less than the z_critical (based on 95% level confidence), it means the z_score_hypothesis is in the rejection region we decided.
  z_critical = stats.norm.ppf(alpha)
  
if z_score > z_critical:
  print("There is no evidence to reject the hypothesis/the sample")
 else:
  print("The sample/hypothesis sample is in the rejection region (based on the decided level of confidence) = this is unlikely to occur")
  
