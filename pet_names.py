import random 

# Program to generate randomized names when you are bored of calling your pet the same thing

beg = ["sn","m", "bab", "po", "sl"]
mid = ["oop", "a", "oosh", "oo", "ok", "uth"]
end = ["er","ie", "ki", "ku", "u"]

name = random.choice(beg) + random.choice(mid) + random.choice(end)

print(name)
