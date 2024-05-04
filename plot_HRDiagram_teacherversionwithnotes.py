"""
This script is a teacher version of the HR diagram plotting script.
It includes notes and explanations for learning points to be metioned at each step
"""
import numpy as np
# ####################################### #
# STEP 1: Import the necessary libraries
# ####################################### #
# TEACHER NOTE: Import the necessary library but don't add the docstrings yet
# we can ask copilot at the end to add the documentation

import pandas as pd
import matplotlib.pyplot as plt

# ####################################### #
# STEP 2: Load the data
# ####################################### #
# TEACHER NOTE: Describe the data to the learners
# Cols: Temperature (K), Luminosity(L/Lo), Radius(R/Ro), Absolute magnitude(Mv), Star type, Star color, Spectral Class
# Link to Data: https://www.kaggle.com/code/salmanhiro/hertzsprung-russell-diagram/notebook
data = pd.read_csv('data/6_class.csv')

# STEP 3: Plot Luminosity Against Temperature (all types together)
#plt.scatter(data['Temperature (K)'], data['Luminosity(L/Lo)'], c='black', s=1)
#plt.show()

# STEP 4: Plot Luminosity Against Temperature NOW ASK COPILOT TO LOG THE AXES
# plot the log10 of the luminosity against the log10 of the temperature
plt.scatter(np.log10(data['Temperature (K)']), np.log10(data['Luminosity(L/Lo)']),
            c='black', s=1)
#plt.show()
# STEP 5: Invert the x-axis
# invert the x-axis so that the hottest stars are on the left
plt.gca().invert_xaxis()
# TEACHER NOTE: if copilot doesn't start giving right answer we can go to copilot chat
#plt.show()

# STEP 6: Add labels and title [COPILOT SHOULD GIVE YOU THE CODE WITH COMMENT BELOW]
# add axis labels
plt.xlabel('Log10(Temperature (K))')
plt.ylabel('Log10(Luminosity(L/Lo))')
plt.title('HR Diagram')
#plt.show()

# STEP 7: Make masks for all the spectral classes
O_mask = data['Spectral Class'] == 'O'
B_mask = data['Spectral Class'] == 'B'
A_mask = data['Spectral Class'] == 'A'
F_mask = data['Spectral Class'] == 'F'
G_mask = data['Spectral Class'] == 'G'
K_mask = data['Spectral Class'] == 'K'
M_mask = data['Spectral Class'] == 'M'

# make a fictionary relating spectral class to color [COPILOT GAVE ME THE CODE!]
colors = {'O': 'blue', 'B': 'cyan', 'A': 'green', 'F': 'yellow', 'G': 'orange', 'K': 'red', 'M': 'brown'}

# plot the HR diagram with different spectral classes in different colors
plt.figure()
plt.scatter(np.log10(data['Temperature (K)'][O_mask]), np.log10(data['Luminosity(L/Lo)'][O_mask]),
            c=colors['O'], s=10, label='O')
plt.scatter(np.log10(data['Temperature (K)'][B_mask]), np.log10(data['Luminosity(L/Lo)'][B_mask]),
            c=colors['B'], s=10, label='B')
plt.scatter(np.log10(data['Temperature (K)'][A_mask]), np.log10(data['Luminosity(L/Lo)'][A_mask]),
            c=colors['A'], s=10, label='A')
plt.scatter(np.log10(data['Temperature (K)'][F_mask]), np.log10(data['Luminosity(L/Lo)'][F_mask]),
            c=colors['F'], s=10, label='F')
plt.scatter(np.log10(data['Temperature (K)'][G_mask]), np.log10(data['Luminosity(L/Lo)'][G_mask]),
            c=colors['G'], s=10, label='G')
plt.scatter(np.log10(data['Temperature (K)'][K_mask]), np.log10(data['Luminosity(L/Lo)'][K_mask]),
            c=colors['K'], s=10, label='K')
plt.scatter(np.log10(data['Temperature (K)'][M_mask]), np.log10(data['Luminosity(L/Lo)'][M_mask]),
            c=colors['M'], s=10, label='M')
plt.gca().invert_xaxis()
plt.xlabel('Log10(Temperature (K))')
plt.ylabel('Log10(Luminosity(L/Lo))')
plt.title('HR Diagram')
plt.legend()
#plt.show()

# STEP 8: Use the class in utils.py to plot the HR diagram
# TEACHER NOTE: this is to show that copilot knows about stuff you've written in other files
from utils import HRDiagram
myhrd_object = HRDiagram(data='data/6_class.csv')
myhrd_object.plot_HR_diagram()
#plt.show()

# STEP 9: Show a Unitest for the HRDiagram class in test_teacherversionwithnotes.py
# TEACHER NOTE: In the command line run pytest --verbose

# STEP 10: Add code to raise error in HRDiagram if data doesn't exist and check correct error raised in test
myhrd_object = HRDiagram(data='data/empty.csv')
# LAST STEP: Document the script with copilot!