<script>Javascript</script>
<attribute source="https://github.com/zachwylde00/lifewriter.application.A.I./UI/components/artificial-intelligence.neural-network.py"/>
class NeuralNetwork: 
  def __init__(self, learning_rate):          self.weights = np.array
([np.random.randn(), 
np.random.randn()]) 
            self.bias = np.random.randn() self.learning_rate = learning_rate 
def _sigmoid(self, x):
return 
    1 / (1 + np.exp(-x)) 
def _sigmoid_deriv(self, x):
return 
    self._sigmoid(x) * (1 - self._sigmoid(x)) def predict
(self, input_vector): 
layer_1 = np.dot
(input_vector, self.weights) + self.bias layer_2 = self._sigmoid(layer_1) 
prediction = layer_2 
return 
    prediction 
def _compute_gradients
(self, input_vector, target): 
layer_1 = np.dot
(input_vector, self.weights) + self.bias.    layer_2 =
    self._sigmoid(layer_1) 
  prediction = 
    layer_2 
     derror_dprediction =
    2 * (prediction - target) 
        dprediction_dlayer1 =       self._sigmoid_deriv(layer_1) 
           dlayer1_dbias = 1 
              dlayer1_dweights = 
     (0 * self.weights) + (1 * input_vector) 
                derror_dbias = 
     ( derror_dprediction * dprediction_dlayer1 * dlayer1_dbias ) 
                     derror_dweights = 
      ( derror_dprediction * dprediction_dlayer1 * dlayer1_dweights )     
                          return 
       derror_dbias, derror_dweights 
def
_update_parameters
(self, derror_dbias, derror_dweights): 
      self.bias = 
         self.bias - 
         (derror_dbias * self.learning_rate) 
self.weights = 
   self.weights - 
         ( derror_dweights * self.learning_rate ) 


# create an instance of NeuralNetwork(), and then you call .predict():

class NeuralNetwork: 
# ... 
def 
  train
(self, input_vectors, targets, iterations):      cumulative_errors =
[] for current_iteration inrange(iterations):  
# Pick a data instance at random  random_data_index = np.random.randint
(len(input_vectors)) 
input_vector = input_vectors[random_data_index] 
target =
targets[random_data_index]
# Compute the gradients and update the weights 
derror_dbias, 
   derror_dweights = 
      self._compute_gradients
          (input_vector, target)         self._update_parameters
          (derror_dbias, derror_dweights)
# Measure the cumulative error for all the instances
if current_iteration % 100 == 0:  cumulative_error = 0 
# Loop through all the instances to measure the error
for data_instance_index in 
range(len(input_vectors)): 
         data_point = input_vectors[data_instance_index] 
                  target = targets[data_instance_index] 
           prediction = self.predict(data_point)        
                     error =
np.square(prediction - target) 
cumulative_error = 
   cumulative_error + error 
     cumulative_errors.append
      (cumulative_error)
        return 
          cumulative_errors 

# calculate the partial derivatives and 
# return derivatives for the bias and the weights. They use _compute_gradients()
# update bias and the weights using _update_parameters()= defined in the previous code block
# compute the prediction result.
# compute the error for every instance.
# accumulate the sum of the errors using the cumulative_error variable to plot a point with the error for all data instances. 
# append the error to cumulative_errors, the array that stores the errors. You’ll use this array to plot graph.
# restart the kernel after add train() to the NeuralNetwork class.
# use a dataset with just eight instances= the input_vectors array. 
# can call train() and use Matplotlib to plot the cumulative error for each iteration:
# add the train method to the class) 
# In [46]: import matplotlib.pyplot as plt 
# In [47]: input_vectors = np.array( ...: [ ...: [3, 1.5], ...: [2, 1], ...: [4, 1.5], ...: [3, 4], ...: [3.5, 0.5], ...: [2, 0.5], ...: [5.5, 1], ...: [1, 1], ...: ] ...: ) # targets = np.array([0, 1, 0, 1, 0, 1, 1, 0]) 
# learning_rate = 0.1 
# neural_network=NeuralNetwork(learning_rate) 
# training_error=neural_network.train(input_vectors, targets, 10000) 
# plt.plot(training_error) 
# plt.xlabel("Iterations")
# plt.ylabel("Error for all training instances")
# plt.savefig("cumulative_error.png") 
# instantiate the NeuralNetwork class
# again and call train() using 
# the input_vectors and the target values. # should run 10000 times;
# learning_rate = 0.1 
# neural_network=NeuralNetwork
(learning_rate) 
# neural_network.predict
     (input_vector) 
       Out[44]:
          array([0.79412963]); 

class NeuralNetwork: 
# ... 
def
   train
     (self, input_vectors, targets, iterations): 
        cumulative_errors = 
          [] for current_iteration in range
            (iterations): 
# Pick a data instance at random 
               random_data_index =          np.random.randint
  (len(input_vectors))
      input_vector=
         input_vectors[random_data_index] 
             B  target = 
                  targets
                    [random_data_index] 
# Compute the gradients and update the weights 
     derror_dbias, derror_dweights =       self._compute_gradients
    ( input_vector, target ) self._update_parameters
    (derror_dbias, derror_dweights) 
# Measure the cumulative error for all the instances 
if current_iteration % 100 == 0:           cumulative_error = 0 
# Loop through all the instances to measure the error
     for data_instance_index in. range(len(input_vectors)):
    data_point =   input_vectors[data_instance_index] 
             target = 
targets[data_instance_index]
      prediction = 
self.predict(data_point) 
               error = np.square(prediction - target) 
cumulative_error = 
                 cumulative_error + error 32 cumulative_errors.append(cumulative_error)
  return 
    cumulative_errors 


