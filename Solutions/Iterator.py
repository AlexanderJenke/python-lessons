class Reverse:
    """ Itterator that itterates over a List in the reverse direction"""
    def __init__(self, l: list):
        # store the list we want do go over
        self.list = l

    def __iter__(self):
        # set up the pointer showing where we are in the list to point to the end of the list
        self.i = len(self.list)
        return self  # required by specification of this funktion

    def __next__(self):
        # get next element in list
        self.i -= 1  # move on step to the left
        if self.i < 0:  # check if the left end of the list is reached
            raise StopIteration  # tell the caller the end of list is reached
        return self.list[self.i]  # return current element


l = "Lorem Ipsum"
it = Reverse(l)
for i in it:
    print(i)
