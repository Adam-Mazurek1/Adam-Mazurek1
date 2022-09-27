"""
Created on Mon Sep 26 12:55:22 2022

@author: adammazurek
"""

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np



def read_in_csv(y_vals):
    opened_file = open('/Users/adammazurek/Downloads/MuonLifetimedataCombined - MuonLifetimedata3CSV.csv')
    for line in opened_file:
            placeholder = ''
            comma_has_been_found = 0
            for char in line:
                    if comma_has_been_found:
                        placeholder += char
                    if char ==',':
                        comma_has_been_found = 1
            y_vals.append(int(placeholder))
            

def best_fit_line(y_vals):
    x_vals = list(range(0,len(y_vals)))
    a_guess = 50
    b_guess = -0.01
    c_guess = 0.001
    
    popt, pcov =  curve_fit(lambda t, a, b, c: a * np.exp(b * (t - 0.3)) + c, x_vals, y_vals, p0=(a_guess, b_guess, c_guess))


    print(popt)
    print(pcov)
        
    return popt
    
def plot_data(y_vals, a, b, c):
    x_vals = list(range(0,len(y_vals)))
    y_vals = y_vals
    plt.bar(x_vals, y_vals, width = 1, linewidth = 0, label = "Detector Time Data")
    plt.xlabel('Channel')
    plt.ylabel("Counts")
    
    x = np.linspace(0,1020)
    y = a * np.exp(b*x)+c
    plt.plot(x,y, color = 'red', linewidth = 2, label = "Exponential Fit Regression")
    plt.legend()
    
    
    plt.savefig("Muon_best_fit_line.pdf")

        
def main():
    y_vals = []
    read_in_csv(y_vals)
    a,b,c = best_fit_line(y_vals)
    plot_data(y_vals, a, b, c)
    
main()
