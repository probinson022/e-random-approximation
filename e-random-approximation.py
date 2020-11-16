
import random 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from scipy.stats import describe
sns.set() 



# global variables. Sets number of trials. 
n = 100000
trials = np.arange(1, n, 1000)

# the following function selects a random real number from 
# (0, 1). If the number is less than 1, a second real number
# is randomly selected and added to the first number. This 
# process continues until the sum exceeds 1. The function then 
# returns the number of selections that were made
def random_real():
	s = 0	
	count = 0
	while s < 1:
		r = random.uniform(0, 1)
		s += r
		count +=1 
	return count 

# the following function performs the above procedure
# len(trials) times and appends each result into a list.
# The list contains the selection counts for n trials.
def experiment(trials):
	count_list = []
	for i in range(trials):
		count_list.append(random_real())
	return count_list

# this function provides summary statistics for the LAST
# experiment performed. If n = 1,000, this summary will
# output summary statistics for an experiment with 1000 trials
def summary(n, last_result):
		abs_err = np.abs(np.average(last_result) - np.exp(1)) #absoulte error
		rel_err = abs_err/np.exp(1) # relative error 
		print('Trials: {0}'.format(n))
		print(describe(last_result))
		print('Absolute Error: {0}'.format(abs_err))
		print('Relative Error: {0:%}'.format(rel_err), '\n')

# the main function in this program outputs two graphs meant
# to illustrate the convergence of the average selection counts
# to the number e. The first graph shows the actual approximation
# convergence as the trials tend upward. The second graph shows
# the downward error trend as the average selection count approaches e.
def main(): 
	start = time.time()
	results = [experiment(trial) for trial in trials] # collection of selection count lists 
	averages = [np.average(result) for result in results] # collection of averages for each selection count list 
	abs_err_list = [np.abs(average - np.exp(1)) for average in averages] # list of abs error for each selection count average
	rel_err_list = [abs_err/np.exp(1) for abs_err in abs_err_list] # list of rel error for each selection count average 
	summary(n, results[-1]) # summary statistics as defined above 
	end = time.time()
	print('Runtime: {0}'.format(end - start), '\n') # Records and outputs runtime

	fig = plt.figure()

	# Plots approximation subplot 
	ax1 = plt.subplot(211) 
	plt.title('Approximation to $e$')
	plt.plot(trials, averages, 'b', label='Average Count')
	plt.hlines(y=np.exp(1), xmin=0, xmax=n, color='black', linestyle='dashed', label=r'$e$' )
	plt.ylabel('Average Count', labelpad=10)
	plt.legend()

	# plots abs and rel error subplot 
	ax2 = plt.subplot(212) 
	plt.title('Absolute and Relative Error')
	plt.plot(trials, abs_err_list, color='r', label='Absolute Error')
	plt.plot(trials, rel_err_list, color='g', label='Relative Error')
	plt.xlabel('Trials')
	plt.ylabel('Error', labelpad=10)
	plt.legend()

	plt.tight_layout()
	plt.show()

main()