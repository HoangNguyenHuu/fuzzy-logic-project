from matplotlib import pyplot as plt
import numpy as np


# distance dependency
# distance dependency
def distance_near_dependency(distance):
    if 0 <= distance <= 70:
        return 1.0
    if 70 < distance < 140:
        return (140 - distance) / 70.0
    return 0.0


def distance_medium_dependency(distance):
    if 70 <= distance <= 140:
        return (distance - 70) / 70.0
    if 140 <= distance <= 210:
        return (210 - distance) / 70.0
    return 0.0


def distance_far_dependency(distance):
    if 140 <= distance <= 210:
        return (distance - 140) / 70.0
    if distance >= 210:
        return 1.0
    return 0.0


# evenly sampled time at 200ms intervals
distance1 = np.arange(0., 140., 0.2)
distance2 = np.arange(70., 210., 0.2)
distance3 = np.arange(140., 280., 0.2)

near = [distance_near_dependency(tmp) for tmp in distance1]
medium = [distance_medium_dependency(tmp) for tmp in distance2]
far = [distance_far_dependency(tmp) for tmp in distance3]

# red dashes, blue squares and green triangles

plt.xlabel("Distance")
plt.ylabel("Dependency")

plt.title("Distance dependency")

plt.text(40, 1.0, "near")
plt.text(120, 1.0, "medium")
plt.text(230, 1.0, "far")

plt.plot(distance1, near, distance2, medium, distance3, far)
plt.show()
