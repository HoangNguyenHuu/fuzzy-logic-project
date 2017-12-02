from matplotlib import pyplot as plt
import numpy as np


def lamp_red_dependency(time):
    if time >= 6:
        return 1.0
    if 3 <= time <= 6:
        return (time - 3) / 3.0
    return 0.0


def lamp_less_red_dependency(time):
    if time <= 3:
        return 1.0
    if 3 <= time <= 6:
        return (6 - time) / 3.0
    return 0.0


time1 = np.arange(0., 6., 0.1)
time2 = np.arange(3., 20., 0.1)

less_red = [lamp_less_red_dependency(tmp) for tmp in time1]
red = [lamp_red_dependency(tmp) for tmp in time2]

# red dashes, blue squares and green triangles

plt.xlabel("Time Red Lamp")
plt.ylabel("Dependency")

plt.title("Red dependency")

plt.text(1, 1.0, "less red")
plt.text(9, 1.0, "red")

plt.plot(time1, less_red, time2, red)
plt.show()
