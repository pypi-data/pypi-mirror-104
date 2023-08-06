# Please note this is a community distribution of allegro5 project, you can find the official github repository [here](https://github.com/liballeg/allegro5)

This package was made for those how can't build this allegro5's binaries themselves or make the python wrapper using cmake.

> Allegro is a cross-platform library mainly aimed at video game and multimedia programming. It handles common, low-level tasks such as creating windows, accepting user input, loading data, drawing images, playing sounds, etc. and generally abstracting away the underlying platform...

And it's now available in python (wrapped using ctypes).
This wrapper was built from the [official github repo](https://github.com/liballeg/allegro5/tree/5.0.10-pre) using cmake (version 5.0.10)

- tested on **windows 10**

N.B
---
Note that this library currently only supports **32-bit** python compilers on **windows**. Please contact me  if you want to add Platform specific support. 

Demo script
----
```py
from allegro import *
al_run_demo()
```

The demo game is hosted [here](https://github.com/liballeg/allegro5/blob/master/python/pong.py) 

Documentation
------
You can find official documentation [here](https://www.allegro.cc/manual/5/)