from numpy import exp, array, random, dot, shape

data_size = 100

data = []
for i in range(data_size):
    data.append([1/random.randint(1,5), 1/random.randint(1,5)])

target = []
for i in data:
    target.append(i[0] * i[1])


synapses = 2 * random.random((2,1)) - 1

for i in range(50000):
    weighted_sum = dot(data, synapses)
    output = 1/(1+exp(-weighted_sum))
    error = 0.5 * ((target - output) ** 2)
    adjustment = -(target - output) * output * (1-ouput) * output
    synapses = synapses - adjustment


print("Target Outputs: ")
print(target)

print("Neural Network Output: ")
print(1/(1+exp(-dot(data, synapses))))
