# -*- coding: utf-8 -*-

#%% 

import numpy as np
import matplotlib.pyplot as plt

def bmi(file_name):
    data = np.loadtxt(file_name, delimiter=',')
    
    weight = data[0,:]
    height = data[1,:]
    height = height/100
    
    n = 0
    how_many = len(weight)
    BMI_data = np.zeros((how_many,1))
    
    for n in range(0, how_many):
            BMI_data[n] = weight[n]/((height[n])**2)
            n = n + 1
       
    sum_1 = 0
    sum_2 = 0
    
    for x in BMI_data:
        if x < 17:
            sum_1 = sum_1 + 1            
        elif x > 30:
            sum_2 = sum_2 + 1
            
    print('%d people with BMI below 17' % sum_1)
    print('%d people with BMI above 30' % sum_2)            
    
    plt.figure(figsize=(16, 14))
    
    plt.subplot(2, 2, 1)
    plt.hist(height, label='HEIGHTS', color='g', orientation='horizontal', bins=15)
    plt.legend()
    plt.title('HEIGHTS')
    plt.ylabel('Heigth [cm]')
    
    plt.subplot(2, 2, 2)
    plt.scatter(weight,height, color='red', label='WEIGHTS vs HEIGHTS', zorder=2)
    plt.ylabel('Height [cm]')
    plt.xlabel('Weight [kg]')
    plt.title('WEIGHTS vs HEIGHTS')
    plt.legend(loc=1)
    
    plt.subplot(2, 2, 4)
    plt.hist(weight, label='WEIGHTS')
    plt.legend()
    plt.title('WEIGHTS')
    plt.xlabel('Weight [kg]')
    
    plt.subplot(2, 2, 3)
    plt.hist(BMI_data, label='BMI')
    plt.legend()
    plt.title('BMI (BODY MASS INDEX)')
    plt.xlabel('$BMI [kg/m^2]$')
    
    splt_name = file_name.split(sep='.')
    save_name = splt_name[0] + '.png'
    plt.savefig(save_name)