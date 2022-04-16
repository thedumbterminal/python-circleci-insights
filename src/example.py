import time
import random

def quick():
    return 1

def slow():
    time.sleep(10)
    return 10

def flaky():
    return random.randint(0, 2)
