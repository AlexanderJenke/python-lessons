import matplotlib.pyplot as plt
import numpy as np
import pickle

data_file_name = '../Data/Niederschlag_data.npy'
header_file_name = '../Data/Niederschlag_header.pkl'

if __name__ == '__main__':
    data = np.load(data_file_name)

    with open(header_file_name, 'rb') as header_file:
        header = pickle.load(header_file)

    # Maskiere die Stellen in den Daten, wo keine Werte gemessen wurden
    # dadurch werden sie von pyplot ignoriert.
    masked_data = np.ma.masked_equal(data, header['nodataflag'])

    plt.imshow(masked_data)
    plt.show()
