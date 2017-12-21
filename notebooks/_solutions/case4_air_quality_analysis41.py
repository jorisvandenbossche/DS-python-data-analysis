fig, axfr = plt.subplots()
FR_scaled.plot(use_index=False, ax = axfr)  #alternative version: FR_scaled.reset_index(drop=True).plot(use_index=False)  
axfr.set_ylabel('FR04012')
# optional addition, just in case you need this
axfr.axvline(x=FR_scaled.searchsorted(0.3), color='0.6', linestyle='--', linewidth=3)