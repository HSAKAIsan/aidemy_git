#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  random
with  open("./hyakunin.txt", encoding="utf-8") as  f:
    wakas = [s.strip() fors inf.readlines()]
print(wakas[random.randrange(len(wakas))])