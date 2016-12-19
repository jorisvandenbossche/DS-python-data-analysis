x, y = b_data[:,3], b_data[:,4] 
t = np.polyfit(x, y, 4) # fit a 2nd degree polynomial to the data, result is x**2 + 2x + 3
t
x.sort()
plt.plot(x, y, 'o')
plt.plot(x, t[0]*x**4 + t[1]*x**3 + t[2]*x**2 + t[3]*x +t[4], '-')