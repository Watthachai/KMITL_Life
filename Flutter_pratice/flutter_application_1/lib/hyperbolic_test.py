
import numpy as np
import math
import matplotlib.pyplot as plt

### Hyperbolic functions
in_array = np.linspace(-np.pi, np.pi, 12)
out_array = np.tanh(in_array)

print("in_array", in_array)
print("\nout_array", out_array)


#mathplot lib
plt.plot(in_array, out_array, color = 'red', marker = "o")
plt.title("numpy.tanh()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
