import detect as ml
import makeGraph as graph

#Set Learning Rate (Default: 0.1), Steps (Default: 1000)
learning_rate = 0.1
steps = 1000
a, b, c, r = ml.get_data(learning_rate, steps)
print(a, b, c, r)
graph.make(a, b, c, r)