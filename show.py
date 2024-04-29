#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  random
    with  open("./hyakunin.txt", encoding="utf-8")  as  f:
    wakas = [s.strip() fors inf.readlines()]
print("今日の一句"+ wakas[random.randrange(len(wakas))])