from matplotlib import pyplot as plt
import numpy as np


# angle dependency
def angle_small_dependency(angle):
    if 0 <= angle <= 7:
        return 1.0
    if 7 <= angle <= 14:
        return (14 - angle) / 7.0
    return 0.0


def angle_medium_dependency(angle):
    if 7 <= angle <= 14:
        return (angle - 7) / 7.0
    if 14 <= angle <= 21:
        return (21 - angle) / 7.0
    return 0.0


def angle_big_dependency(angle):
    if angle >= 21:
        return 1.0
    if 14 <= angle <= 21:
        return (angle - 14) / 7.0
    return 0.0


angle1 = np.arange(0., 14., 0.1)
angle2 = np.arange(7., 21., 0.1)
angle3 = np.arange(14., 28., 0.1)

small = [angle_small_dependency(tmp) for tmp in angle1]
medium = [angle_medium_dependency(tmp) for tmp in angle2]
big = [angle_big_dependency(tmp) for tmp in angle3]

# red dashes, blue squares and green triangles

plt.xlabel("Angle")
plt.ylabel("Dependency")

plt.title("Angle dependency")

plt.text(3, 1.0, "small")
plt.text(12, 1.0, "medium")
plt.text(22, 1.0, "big")

plt.plot(angle1, small, angle2, medium, angle3, big)
plt.show()