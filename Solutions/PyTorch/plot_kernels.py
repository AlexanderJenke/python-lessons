import torch
import matplotlib.pyplot as plt
import torchvision
import numpy as np

if __name__ == '__main__':
    path = "MNIST_SVM_3.pt"
    state_dict = torch.load(path)
    img = torchvision.utils.make_grid(state_dict["conv1.weight"], nrow=5, normalize=True)
    plt.title(path)
    plt.imsave(path.split('.')[0] + ".png", np.einsum('chw->hwc', img.numpy()))
