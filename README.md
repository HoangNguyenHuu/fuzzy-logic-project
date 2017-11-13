 Self Driving Car - Fuzzy Logic

This is a project of IT4844 credit at Hanoi University of Science and Technology (HUST)

### Prerequisites

This project write by **PyCharm IDE**, you can open it by Pycharm (or other python IDE)

You need install python 3 for run this project. Moreover, you need install libraries:
* [Pygame] (https://www.pygame.org/news)
* [Scipy] (https://www.scipy.org/)
* [xlrd] (https://pypi.python.org/pypi/xlrd)

```
In Ubuntu, you can install it by command line (before this, you need install python 3 and pip3):

sudo pip3 install scipy

sudo pip3 install xlrd

sudo pip3 install pygame



(some time it not work (especially the Pygame library), maybe you need some other libraries, you can Google for know how to install these packages)
```

## Running the tests

Run file **run.py** in package **main**

You can change other map by change line 27 in file **run.py**: "map_s.add(maps.Map(0, 0, 1))" -
the third parameter in (0, 0, 1) above is ordinal number of map, you can change 1 by 2, 3 for other map.
