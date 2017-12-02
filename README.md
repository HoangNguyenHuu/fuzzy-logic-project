# Self Driving Car - Fuzzy Logic

This is a project of subject IT4844 at Hanoi University of Science and Technology (HUST)

### Prerequisites

This project is writen with **PyCharm IDE**, you can open it with Pycharm (or any other python IDE)

You need install python 3 for run this project. Moreover, you need install libraries:
* [Pygame] (https://www.pygame.org/news)
* [Scipy] (https://www.scipy.org/)
* [xlrd] (https://pypi.python.org/pypi/xlrd)

```
In Ubuntu, you can install this by command line (before this, you need to install python 3 and pip3):

sudo pip3 install scipy

sudo pip3 install xlrd

sudo pip3 install pygame



(Sometimes it may not work (especially the Pygame library), maybe you need some other libraries! You can google to know how to install these packages)
```

## Run this project

- Run file **run.py** in package **main**

- You can change to any other map by change line 27 in file **run.py**: "map_s.add(maps.Map(0, 0, 1))" -
the third parameter in (0, 0, 1) is the ordinal number of map, you can change 1 by 2, 3 for any other map.

- Add or remove obstacle on click
