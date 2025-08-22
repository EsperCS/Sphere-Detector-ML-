#SPHERE_DETECT: (x-a)^2 + (y-b)^2 + (z-c)^2 = r^2
#               x^2 +y^2 + z^2 -2ax-2by-2cz + a^2+b^2+c^2 = r^2
#               x^2 +y^2 + z^2 -2ax-2by-2cz + d = r^2
#DATA: x, y, z
#TARGET: FIND a, b, c, r
import torch
import torch.nn
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
const_a = torch.tensor([1.0], requires_grad=True)
const_b = torch.tensor([1.0], requires_grad=True)
const_c = torch.tensor([1.0], requires_grad=True)
radius = torch.tensor([1.0], requires_grad=True)
#----------Database----------
def main(learning_rate, steps):
    database = open("database_sphere.txt", "r")

    xAxis_array = []
    yAxis_array = []
    zAxis_array = []
    lines = 0

    for line in database:
        dataLine = line.strip().split(" ")
        xAxis_array.append(float(dataLine[0]))
        yAxis_array.append(float(dataLine[1]))
        zAxis_array.append(float(dataLine[2]))
        lines += 1

    xAxis_tensor = torch.tensor(xAxis_array, dtype = torch.float32)
    yAxis_tensor = torch.tensor(yAxis_array, dtype = torch.float32)
    zAxis_tensor = torch.tensor(zAxis_array, dtype = torch.float32)

    #----------Sphere Equation Function----------
    #(x-a)^2 + (y-b)^2 + (z-c)^2 = r^2
    #x^2 +y^2 + z^2 -2ax-2by-2cz + a^2+b^2+c^2 = r^2
    #x^2 +y^2 + z^2 -2ax-2by-2cz + d = r^2
    #z^2 = r^2 - d + (2ax + 2by + 2cz) - x^2 - y^2
    def calculateSquaredZ_axis(x, y, z, a, b, c, r):
        d = a**2 + b**2 + c**2
        zSquare = r**2 - d + (2*a*x + 2*b*y + 2*c*z) - x**2 - y**2
        return zSquare
    #---------
    optimizer = torch.optim.Adam([const_a, const_b, const_c, radius], lr = learning_rate)
    loss_fn = torch.nn.MSELoss()
    #----------Main Loop----------
    for step in range(steps):
        optimizer.zero_grad()
        squared_zAxis_hat = calculateSquaredZ_axis(xAxis_tensor, yAxis_tensor, zAxis_tensor, const_a, const_b, const_c, radius)
        loss = loss_fn(squared_zAxis_hat, zAxis_tensor**2)
        loss.backward()
        optimizer.step()
    #print(const_a.item(), const_b.item(), const_c.item(), radius.item())

def get_data(learning_rate, steps):
    main(learning_rate, steps)
    return [const_a.item(), const_b.item(), const_c.item(), radius.item()]

#----------Show Data----------
