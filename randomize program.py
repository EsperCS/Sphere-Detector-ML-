import random
import math

f = open("database_sphere.txt", "w")
x0 = random.uniform(1, 10)
y0 = random.uniform(1, 10)
z0 = random.uniform(1, 10)
r = random.uniform(20, 30)

for _ in range(50):
    # sinh góc
    theta = random.uniform(0, math.pi)
    phi = random.uniform(0, 2*math.pi)
    x = r * math.sin(theta) * math.cos(phi) + x0
    y = r * math.sin(theta) * math.sin(phi) + y0
    z = r * math.cos(theta) + z0
    f.write(f"{x:.2f} {y:.2f} {z:.2f}\n")

f.close()
