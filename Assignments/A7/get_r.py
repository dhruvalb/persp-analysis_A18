import numpy as np

def get_r(K, L, alpha, Z, delta):
	'''
	Function generates the interest rate or vector of interest rates
	'''
	r = alpha * Z * ((L/K)**(1 - alpha)) - delta

	return r
