import torch
from dataset import MNIST
from torch.utils.data import DataLoader
from model import Net
from torch.optim import Adam
from torch.optim.lr_scheduler import OneCycleLR
import torch.nn as nn
from tqdm import tqdm
import numpy as np
import tensorboardX
from sklearn.metrics import f1_score

N_EPOCHS = 100
N_CLASSES = 10
BATCH_SIZE = 1000
MAX_LR = 1e-4

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


if __name__ == '__main__':
    # load datasets
    trainset = MNIST("../../Data/MNIST/test/")
    testset = MNIST("../../Data/MNIST/test/")

    trainloader = DataLoader(trainset, batch_size=BATCH_SIZE, shuffle=True)
    testloader = DataLoader(testset, batch_size=BATCH_SIZE, shuffle=False)

    # init Model
    model = Net()
    model = model.to(device)

    # init optimizer, lr_sched & loss
    optimizer = Adam(model.parameters(), lr=MAX_LR)
    scheduler = OneCycleLR(optimizer, max_lr=MAX_LR, epochs=100, steps_per_epoch=len(trainloader))
    nllloss = nn.NLLLoss()

    log = tensorboardX.SummaryWriter("MNIST_SVM_3_3")

    # train
    for epoch in range(N_EPOCHS):
        mean_loss = []
        lables_cat = torch.empty(0, dtype=torch.long)
        output_cat = torch.empty(0, dtype=torch.long)
        for batch in tqdm(trainloader, desc=f"Train {epoch}", leave=False):
            # move data to gpu
            img_cpu, label_cpu = batch
            img = img_cpu.to(device)
            label = label_cpu.to(device)

            # let model predict results
            output = model(img)

            # calc loss
            loss = nllloss(output, label)
            mean_loss.append(loss.cpu().item())

            # backpropagate loss & adjust model
            loss.backward()
            optimizer.step()
            scheduler.step()

            # collect data for the f1 score
            lables_cat = torch.cat((lables_cat, label_cpu))
            output_cat = torch.cat((output_cat, output.argmax(axis=1).cpu()))

        # calculate the f1 score
        train_f1 = f1_score(lables_cat, output_cat, average='macro')

        lables_cat = torch.empty(0, dtype=torch.long)
        output_cat = torch.empty(0, dtype=torch.long)
        for batch in tqdm(testloader, desc=f"Test {epoch}", leave=False):
            img_cpu, label_cpu = batch
            img = img_cpu.to(device)
            label_1hot = []

            output = model(img)

            # collect data for the f1 score
            lables_cat = torch.cat((lables_cat, label_cpu))
            output_cat = torch.cat((output_cat, output.argmax(axis=1).cpu()))

        # calculate the f1 score
        test_f1 = f1_score(lables_cat, output_cat, average='macro')

        # write parameters to log
        log.add_scalar("Train F1", train_f1, global_step=epoch)
        log.add_scalar("Test F1", test_f1, global_step=epoch)
        log.add_scalar("Loss", np.mean(mean_loss), global_step=epoch)
        log.add_scalar("LR", scheduler.get_lr()[0], global_step=epoch)
        print(f"{epoch}: "
              f"train f1 {train_f1*100:.2f}%, "
              f"test f1 {test_f1*100:.2f}% "
              f"loss {np.mean(mean_loss):.3f}", flush=True)

    # close log
    log.close()

    # save model
    model.save("MNIST_SVM_3.pt")
