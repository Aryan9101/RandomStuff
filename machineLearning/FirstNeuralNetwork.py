from numpy import exp, array, random, dot, shape


class NeuralNetwork():
    def __init__(self):
        random.seed(1)
        self.synaptic_weights = 2 * random.random((2, 1)) - 1

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            output = self.think(training_set_inputs)

            error = training_set_outputs - output

            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
            

            self.synaptic_weights = self.synaptic_weights + adjustment

    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

data_size = 500        

def generate_training_data():
    data = []
    for i in range(data_size):
        data.append([1/random.randint(1,5), 1/random.randint(1,5)])
    return data

def generate_training_output():
    output = []
    for i in generate_training_data():
        output.append(i[0] * i[1])
    return output
        
if __name__ == "__main__":
    neural_network = NeuralNetwork()

    print("Random starting synaptic weights: ")
    print(neural_network.synaptic_weights)

    training_set_inputs = array(generate_training_data())
    training_set_outputs = array(generate_training_output())

    neural_network.train(training_set_inputs, training_set_outputs, 50000)

    print("New synaptic weights after training: ")
    print(neural_network.synaptic_weights)

    print("Outputs")
    print(1/training_set_outputs)

#    print("Considering new situation [1, 1, 1] -> ?: ")
#    print(neural_network.think(array([1, 1, 1])))

    print("Real answer")
    print(1/neural_network.think(array([1,1,1])))

    print("Error")
    print(1/training_set_outputs - 1/neural_network.think(array([1,1,1])))

