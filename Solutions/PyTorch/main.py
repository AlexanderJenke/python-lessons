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

    # init optimizer, lr_sched & loss
    # TODO Initialisiere den Optimizer, den Lernratenscheduler & die Lossfunktion
    optimizer = None
    scheduler = None
    loss_fn = None

    log = tensorboardX.SummaryWriter()

    # train
    for epoch in tqdm(range(N_EPOCHS)):
        mean_loss = []
        for batch in trainloader:
            # TODO Training
            pass

        log.add_scalar("Train Loss", np.mean(mean_loss), global_step=epoch)
        log.add_scalar("LR", scheduler.get_lr()[0], global_step=epoch)

        mean_loss = []
        with torch.no_grad():
            for batch in testloader:
                # TODO Evaluation
                pass

        log.add_scalar("Test Loss", np.mean(mean_loss), global_step=epoch)
