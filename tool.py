import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_inline import backend_inline
import numpy as np

def use_svg_display():
    """Use the svg format to display a plot in Jupyter."""
    backend_inline.set_matplotlib_formats('svg')
    
def set_figsize(figsize=(3.5, 2.5)):
    """Set the figure size for matplotlib."""
    use_svg_display()
    plt.rcParams['figure.figsize'] = figsize
    
def set_axes(axes, xlabel, ylable, xlim, ylim, xscale, yscale, legend):
    """A utility function to set matplotlib axes."""
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylable)
    axes.set_xscale(xscale)
    axes.set_yscale(yscale)
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    if legend:
        axes.legend(legend)
    axes.grid()
# based on d2l  

def plot(X, y=None, xlabel=None, ylabel=None, legend=None, xlim=None,
         ylim=None, xscale='linear', yscale='linear', fmts=('-', 'm--', 'g-.', 'r:'),
            figsize=(3.5, 2.5), axes=None):
    """绘制数据点"""
    if legend is None:
        legend = []
    
    set_figsize(figsize)
    axes = axes if axes else plt.gca()
    
    def has_one_axes(X):
        return (hasattr(X, "ndim") and X.ndim == 1 or isinstance(X, list) and not hasattr(X[0], "__len__"))
    
    if has_one_axes(X):
        X = [X]
        
    if y is None:
        X, y = [[]] * len(X), X
    elif has_one_axes(y):
        y = [y]
    if len(X) != len(y):
        X = X * len(y)
    axes.cla()
    
    for x, y, fmt in zip(X, y, fmts):
        if len(x):
            axes.plot(x, y, fmt)
        else:
            axes.plot(y, fmt)
    
    set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend)
    


   
    
    