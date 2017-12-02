from matplotlib import pyplot as plt
import numpy as np


# distance dependency
def distance_near_dependency(distance):
    if 0 <= distance <= 100:
        return 1.0
    if 100 < distance < 200:
        return (200 - distance) / 100.0
    return 0.0


def distance_medium_dependency(distance):
    if 100 <= distance <= 200:
        return (distance - 100) / 100.0
    if 200 <= distance <= 300:
        return (300 - distance) / 100.0
    return 0.0


def distance_far_dependency(distance):
    if 200 <= distance <= 300:
        return (distance - 200) / 100.0
    if distance >= 300:
        return 1.0
    return 0.0


# evenly sampled time at 200ms intervals
distance1 = np.arange(0., 200., 0.2)
distance2 = np.arange(100., 300., 0.2)
distance3 = np.arange(200., 400., 0.2)

near = [distance_near_dependency(tmp) for tmp in distance1]
medium = [distance_medium_dependency(tmp) for tmp in distance2]
far = [distance_far_dependency(tmp) for tmp in distance3]

# red dashes, blue squares and green triangles

plt.xlabel("Distance")
plt.ylabel("Dependency")

plt.title("Distance dependency")

plt.text(50, 1.0, "near")
plt.text(180, 1.0, "medium")
plt.text(320, 1.0, "far")

plt.plot(distance1, near, distance2, medium, distance3, far)
plt.show()
