import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    random_numbers = np.random.random(1000)
    x_values = range(1000)

    plt.scatter(x_values, random_numbers)
    plt.show()
