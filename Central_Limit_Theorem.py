import scipy.stats as stats
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_style('whitegrid')

#load the data
df = pd.read_csv('Churn_Modelling.csv')

#plot the variable of interest
df["CreditScore"].hist()

#make the sampling distribution
n_sample = 30
n_try = 1000
mean_list = []

for i in range(n_try):    
    test = df.sample(n = n_sample)
    mean_sample = np.mean(test["CreditScore"])
    mean_list.append(mean_sample)
    
#plot the result
pd.DataFrame(mean_list).plot.hist()

# Or with kernel density estimation curve
sns.distplot(pd.DataFrame(mean_list))

print("std of population: ", np.std(df["CreditScore"]))
print("std of sampling distribution: ", np.std(mean_list)/np.sqrt(n_sample))
