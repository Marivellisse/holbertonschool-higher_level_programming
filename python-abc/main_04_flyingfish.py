#!/usr/bin/env python3
from task_04_flyingfish import FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

print(FlyingFish.mro())  # Optional: print method resolution order
