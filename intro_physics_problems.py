"""
1. Dropped ball simulation (1D), constant acceleration (no air-resistance)
1v2: use functions to improve this script!

2. 2D goal kick (2D), constant acceleration
3. ISS in orbit around the Earth (orbital motion, one-force, varying acceleration)
4. Star cluster (still just gravity, but many objects)
"""
import numpy as np
import matplotlib.pyplot as plt
#astropy lets you use units!
NT = 100
times = np.zeros(NT)
heights = np.zeros(NT)
velocities = np.zeros(NT)
print(times.shape)
print(heights.shape)

## set an initial height
## set an initial velocity (zero)
## update the height at a certain time
## update the velocity at a certain time
heights[0] = 20 # meters

## find the height after 1 second
g = -9.8 # m/s^2
times[1] = 1 # seconds
velocities[1] = g*times[1]
heights[1] = heights[0] + velocities[0]*times[1] + 0.5*g*times[1]**2
print(heights[1])

now = 1
while heights[now] > 0:
    now += 1
    times[now] = times[now-1] + 0.5

    velocities[now] = g*times[now]
    heights[now] = heights[0] + velocities[0]*times[now] + 0.5*g*times[now]**2
    print("heights[now]: ", heights[now])

indices = np.where(heights > 0)
print(indices[0])
heights = heights[indices[0]]
velocities = velocities[indices[0]]
times = times[indices[0]]
print("times: ", times)
print("heights: ", heights)
print("velocities: ", velocities)

fig,axs = plt.subplots(2)
axs[0].plot(times, heights, color="blue", label="height")
axs[1].plot(times, velocities, color="green", label="velocity")
#axs[0].legend()
axs[1].set_xlabel("time [s]")
axs[0].set_ylabel("height [m]")
axs[1].set_ylabel("velocity [m/s]")
plt.savefig("dropped_ball.png")
plt.close()