import time

#implementasi "linear_congruential_generator" atau apalah itu
def lcg(seed, a=1664525, c=1013904223, m=2**32):
    while True:
        seed = (a * seed + c) % m
        yield seed

#Men-generate angka random
def random_generator(seed, low, high):
    load = lcg(seed)
    while True:
        scaled_random = low + next(load) % (high - low + 1)
        yield scaled_random

#function ngeluarin angka randomnya
def random_int (m,n):
    seed=(int(time.time())//1)
    rng = random_generator(seed,m,n)
    for i in range (9):
        a=next(rng)
    return a