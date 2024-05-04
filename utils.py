"""
Name: utils.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# utilities we can create
# -> make the log columns
# make a function to plot HRD diagram for a given star type

class HRDiagram(object):
    def __init__(self, data='data/6_class.csv'):

        self.data = pd.read_csv(data) # written by copilot
        # if data is empty raise an error
        if self.data.empty:
            raise ValueError('HRDIAGRAM: Data is empty')

        self.data['log_T'] = np.log10(self.data['Temperature (K)']) # written by copilot
        self.data['log_L'] = np.log10(self.data['Luminosity(L/Lo)']) # written by copilot
        self.colors = {'O': 'blue', 'B': 'cyan', 'A': 'green', 'F': 'yellow', 'G': 'orange', 'K': 'red', 'M': 'brown'} # written by copilot

    def plot_HR_diagram(self,
                        ax=None,
                        ):
        if ax is None:
            ax = plt.gca()

        for spectral_class in 'OBAFGKM':
            mask = self.data['Spectral Class'] == spectral_class
            ax.scatter(self.data['log_T'][mask], self.data['log_L'][mask],
                       c=self.colors[spectral_class], s=10, label=spectral_class)

        ax.invert_xaxis() # I ADDED THIS LINE
        ax.set_xlabel('Log10(Temperature (K))')
        ax.set_ylabel('Log10(Luminosity(L/Lo))')
        ax.set_title('HR Diagram')
        ax.legend()
        return ax