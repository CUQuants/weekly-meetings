import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# create 1000 equally spaced points between -10 and 10
x = np.linspace(-10, 10, 15)

# calculate the y value for each element of the x vector
y1 = - x**2 + 2*x + 2  

#make a new linspace for our stepper function
x1 = np.linspace(-10, 10, len(x) * 2)

#then create something to hold the y values
y2 = []

#loop through the number of spaces in the linspace
for i in range(len(x)):
    
    #increment by 1
    add = i + i
    
    #I add it in twice to sort flatten the curve at each step
    y2.append(add)
    y2.append(add)

#plot them using 2 subplots
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (24,10))

#plot on the left hand side
ax1.plot(x, y1)
ax1.set_title("Smooth Function", fontsize = 20)
ax1.axis("off")

#plot on the right hand side
ax2.plot(x1, y2)
ax2.set_title("Zoomed in smooth function", fontsize = 20)
ax2.axis("off")

#show the plot
plt.show()

#for the stochcastic process

#we wnat to pull from a normal distribution
from scipy.stats import norm

# Process parameters
delta = 0.5
dt = 0.1

# Initial condition.
x = 0.0

# Number of iterations to compute.
n = 10000

y2 = []

# Iterate to compute the steps of the Brownian motion.
for k in range(n):
    x = x + norm.rvs(scale=delta**2*dt)
    y2.append(x)
    
y3 = []

# Iterate to compute the steps of the Brownian motion.
for k in range(n):
    x = x + norm.rvs(scale=delta**2*dt)
    y3.append(x)
    
#same idea with plotting as above

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (24,10))
ax1.plot(y2)
ax1.set_title("Stochastic Process", fontsize = 20)
ax1.axis("off")
ax2.plot(y3)
ax2.set_title("Zoomed in Stochastic Process", fontsize = 20)
ax2.axis("off")
plt.show()