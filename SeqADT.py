## @SeqADT.py
#  @title Seq ADT
#  @author Xiangxin Kong
#  @date 2/11 2019


## @brief repersent ADT
class SeqADT:
    ## @brief Constructor for SeqADT
    #  @param list of choices
    def __init__(self, x):
        self.s = x
        self.i = 0

    ## @brief reset the i and start from the first one
    def start(self):
        self.i = 0

    ## @brief output next items in the list
    def next(self):
        if self.end():
            raise StopIteration
        self.i = self.i + 1
        return self.s[self.i - 1]

    ## @brief output whether i is out of index
    def end(self):
        return self.i >= len(self.s)
