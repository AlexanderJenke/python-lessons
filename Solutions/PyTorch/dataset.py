import torch
from PIL import Image
import os
from tqdm import tqdm
import numpy as np


class MNIST(torch.utils.data.Dataset):
    def __init__(self, path):
        self.data = []

        for label in tqdm(range(10), desc="loading dataset"):
            for file in os.listdir(os.path.join(path, f"{label}")):
                if not file.endswith(".jpg"):
                    continue

                with open(os.path.join(path, f"{label}", file), "rb") as fd:
                    img = Image.open(fd)
                    img_np = np.asarray(img.getdata(), dtype=np.float32).reshape((1, 28, 28))

                self.data.append((img_np, label))

    def __getitem__(self, item):
        return self.data[item][0], self.data[item][1]

    def __len__(self):
        return len(self.data)
