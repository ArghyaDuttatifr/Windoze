from numpy.random import default_rng
rng = default_rng()
vals = rng.uniform(size=20)
res= vals > 0.5
print (res)