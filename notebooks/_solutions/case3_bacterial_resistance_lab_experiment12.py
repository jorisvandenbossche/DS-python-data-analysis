def errorbar(x, y, low, high, **kws):
    """Utility function to link falcor data representation with the errorbar representation"""
    plt.errorbar(x, y, (y - low, high - y), capsize=3, fmt="o", color="black", ms=4)