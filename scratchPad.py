#!/usr/bin/env

from gameResources import emojis
from random import randint



for i in range(1, 50):
    n = randint(1,len(emojis))
    st = "(" + emojis[str(n)] + ")> "
    print(st)
