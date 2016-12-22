# -*- coding: utf-8 -*-
"""

@author: Stijnvh
"""

import sys
import datetime

import numpy as np
from scipy import stats
from scipy.stats import linregress

import pandas as pd
from pandas.tseries.offsets import DateOffset
from pandas.stats.moments import rolling_std

import pylab as p
import matplotlib as mpl
mpl.rcParams['mathtext.default'] = 'regular'
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Rectangle
from matplotlib.ticker import MaxNLocator

##-----------------------------------------------------------------------------
## Calculating objective functions
##-----------------------------------------------------------------------------
    
def root_mean_square_error(observed, modelled):
    '''
    Root Mean Square Error (RMSE)

    Parameters
    -----------
    observed : np.ndarray or pd.DataFrame
        observed/measured values of the variable
    observed : np.ndarray or pd.DataFrame
        simulated values of the variable

    Notes
    -------        
    The root mean square error is an absolute criterion that is often. 
    It indicates the overall agreement between predicted and observed data. 
    The square allows avoiding 
    error compensation and emphasises larger errors. The root provides 
    a criterion in actual units. Consequently, this quality criterion 
    can be compared to the MAE to provide information on the prominence 
    of outliers in the dataset. 
        
    Notes
    -------
    * range: [0, inf]
    * optimum: 0
    '''
    residuals = observed - modelled
    return np.sqrt((residuals**2).mean())


def bias(observed, modelled):
    """
    Bias E[obs-mod]

    Parameters
    -----------
    observed : np.ndarray or pd.DataFrame
        observed/measured values of the variable
    observed : np.ndarray or pd.DataFrame
        simulated values of the variable
        
    Notes
    -------
    * range: [-inf, inf]
    * optimum: 0
    """
    residuals = observed - modelled      
    return np.mean(residuals)

##-----------------------------------------------------------------------------
## MODEL CALIBRATION EVALUATION PLOTS - SPREAD DIAGRAMS
##-----------------------------------------------------------------------------   

def spread_diagram(axs, obs, mod, infobox = True, *args, **kwargs):
    '''
    plot a scatter plot comparing the simulated and observed datasets in a 
    scatter plot with some extra information about the fit included.
    
    Parameters
    -----------
    axs : axes.AxesSubplot object
        an subplot instance where the graph will be located,
        this supports the use of different subplots
    obs : ndarray
        1D array of the observed data
    mod : ndarray
        1D array of the modelled output
    infobox : bool True|False
        defines if a infobox with the regression info is added or not
    *args, **kwargs : args
        argument passed to the matplotlib scatter command
    
    Returns
    --------
    axs   
    '''
    p.rc('mathtext', default = 'regular')    
       
    axs.scatter(obs,mod, *args, **kwargs)
    axs.set_aspect('equal')
    
    if isinstance(obs, np.ndarray):
        getmax = min(obs.max(), mod.max())*0.9
        getmin = max(obs.min(), mod.min())*1.1
    else:
        getmax = min(obs.max().values, mod.max().values)*0.9
        getmin = max(obs.min().values, mod.min().values)*1.1
        obs = obs.values
        mod = mod.values
    
    axs.plot([getmin, getmax], [getmin, getmax],'k--', linewidth = 0.5)
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(obs, mod)
    
    forplot = np.arange(getmin, getmax, 0.01)
    axs.plot(forplot, slope*forplot + intercept, '-', color = 'grey', 
             linewidth = 0.5)  
    axs.set_xlim(left = getmin, right = getmax)
    axs.set_ylim(bottom = getmin, top = getmax)   
    
    rmse = root_mean_square_error(obs, mod)
    
    #for infobox
    if infobox == True:
        patch = Rectangle((0., 0.65), 0.35, 0.35, facecolor = 'white',
                        edgecolor = 'k', transform = axs.transAxes)
        axs.add_patch(patch)
        axs.set_axisbelow(True)
        
        textinfo = ({'transform' : axs.transAxes, 
                     'verticalalignment' : 'center', 
                     'horizontalalignment' : 'left', 
                     'fontsize' : 12})
                  
        axs.text(0.05, 0.95, r'$\bar{x}\ $', textinfo) 
        axs.text(0.05, 0.90, r'$\bar{y}\ $', textinfo)           
        axs.text(0.05, 0.85, r'$rico\ $', textinfo)             
        axs.text(0.05, 0.8, r'$intc.\ $', textinfo)  
        axs.text(0.05, 0.75, r'$R^2\ $', textinfo)               
        axs.text(0.05, 0.70, r'$RMSE\ $', textinfo)   
    
        axs.text(0.2, 0.95, r': %.2f'%obs.mean(), textinfo) 
        axs.text(0.2, 0.90, r': %.2f'%mod.mean(), textinfo)           
        axs.text(0.2, 0.85, r': %.2f'%slope, textinfo)             
        axs.text(0.2, 0.8, r': %.2f'%intercept, textinfo)  
        axs.text(0.2, 0.75, r': %.2f'%r_value, textinfo)                          
        axs.text(0.2, 0.70, r': %.2f'%rmse, textinfo)    

    return axs


def main(argv=None):
    print(argv[0])
    
    # loading data from a file
    data = pd.read_csv(argv[1], parse_dates=True,               index_col=0).dropna()
    
    # using custom plot function
    
    formatfig = argv[2]
    fig, ax = plt.subplots()
    spread_diagram(ax, data.iloc[:,0].values, 
                   data.iloc[:,1].values, infobox = True)
    fig.savefig("{}_evaluation.{}".format(datetime.date.today().strftime("%Y%m%d"), formatfig))
    

if __name__ == "__main__":
    sys.exit(main(sys.argv))   

