import os, replicate, random, json, time
import ai1, ai2, ai3


you = input("sapa mereka : ")

awal_cakap = [
    lambda: ai1.respon(you),

]

get_awalCakap = random.choice(awal_cakap)

get_awalCakap()