#! /usr/bin/env python3

from tkinter import *
from skimage.transform import downscale_local_mean
from threading import Thread
import time
import torch
import numpy as np
from model import Net


class PaintBox(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.img = np.zeros((280, 280))
        self.pack(expand=YES, fill=BOTH)
        self.master.title("MNIST Predictor")
        self.master.geometry("280x280")

        self.text = Text(self, height=1, width=30)
        self.text.insert(END, "?")
        self.text.pack(side=TOP)

        self.button = Button(self, fg="red", text="Clear", command=self.clear)
        self.button.pack(side=BOTTOM)

        # create Canvas component
        self.canvas = Canvas(self)
        self.canvas.pack(expand=YES, fill=BOTH)

        # bind mouse dragging event to Canvas
        self.canvas.bind("<B1-Motion>", self.paint)

    def clear(self):
        self.img[:, :] = 0
        self.canvas.delete("all")

    def paint(self, event):
        size = 10
        x1, y1 = (event.x - size), (event.y - size)
        x2, y2 = (event.x + size), (event.y + size)
        self.canvas.create_oval(x1, y1, x2, y2, fill="red")
        self.img[event.x - size:event.x + size, event.y - size:event.y + size] = 1


def predict_number(pb):
    while 1:
        try:
            pb.canvas.winfo_exists()
            img = downscale_local_mean(pb.img, (10, 10))
            img_np = np.asarray(img.transpose(), dtype=np.float32).reshape((1, 28, 28))

            rep = np.tile(img_np, (10, 1, 1, 1))

            with torch.no_grad():
                output = model(torch.tensor(rep))

            pred = output.mean(axis=0)
            res = pred.argmax()

            pb.text.delete(1.0, 1.10)
            pb.text.insert(INSERT, f"{res}")

            time.sleep(0.1)
        except:
            print("done")
            break


if __name__ == "__main__":
    model = Net()
    model.load("MNIST_Classifier.pt")
    pb = PaintBox()
    t = Thread(target=predict_number, args=(pb,))
    t.start()
    pb.mainloop()
