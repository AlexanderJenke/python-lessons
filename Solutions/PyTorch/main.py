import torch
from dataset import MNIST
from torch.utils.data import DataLoader
from model import Net
from torch.optim import SGD
from torch.optim.lr_scheduler import OneCycleLR
import torch.nn as nn
from tqdm import tqdm
import numpy as np
import tensorboardX

N_EPOCHS = 100
NAME = "MNIST"
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

if __name__ == '__main__':
    # load datasets
    # TODO lade Test- & Traindaten
    trainset = None
    testset = None

    trainloader = None
    testloader = None

    # init Model
    # TODO Initislisiere das Model und lade es auf die Grafikkarte
    model = None

    # init optimizer, lr_sched & loss
    # TODO Initialisiere den Optimizer, den Lernratenscheduler & die Lossfunktion
    optimizer = None
    scheduler = None
    loss_fn = None

    # Train multiple epochs
    for epoch in range(N_EPOCHS):

        # TRAIN
        mean_loss = []
        for batch in trainloader:
            # move data to gpu
            # TODO
            img_cpu, label_cpu = batch
            img = None
            label = None

            # let model predict results
            # TODO
            output = None

            # calculate the loss
            # TODO
            loss = None
            mean_loss.append(loss.cpu().item())

            # backpropagate loss & adjust model
            # TODO

        # EVALUATE
        lables_cat = torch.empty(0, dtype=torch.long)
        output_cat = torch.empty(0, dtype=torch.long)
        for batch in testloader:
            # move data to gpu
            # TODO
            img_cpu, label_cpu = batch
            img = None
            label = None

            # let model predict results
            # TODO
            output = None

            # collect data for the f1 score
            lables_cat = torch.cat((lables_cat, label_cpu))
            output_cat = torch.cat((output_cat, output.argmax(axis=1).cpu()))

        # calculate the f1 score
        # TODO
        test_f1 = None

        # write log to console
        print(f"{epoch}: "
              f"loss {np.mean(mean_loss):.3f}"
              f"test f1 {test_f1*100:.2f}% ", flush=True)

    # save model
    # TODO
