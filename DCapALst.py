## @DcapALst.py
#  @title Department Capacity
#  @author Xiangxin Kong
#  @date 2/11 2019

## @brief This class create a dictionary of deparment capacity


class DCapAlst:
    ## @brief constructor, initialize the dictionary s
    def __init__(self):
        self.s = {}

    ## @brief add a new department with capacity
    #  @param name of the department
    #  @param capacity number
    def add(self, dept, cap):
        if self.elm(dept):
            raise KeyError
        self.s[dept] = cap

    ## @brief remove a department
    #  @param department
    def remove(self, dept):
        if not self.elm(dept):
            raise KeyError
        self.s.pop(dept)

    ## @brief whether the deparment is in the list
    #  @return boolean result
    def elm(self, dept):
        return dept in self.s

    ## @brief capacity of given department
    #  @param department name
    #  @return capacity of the department
    def capacity(self, dept):
        if not self.elm(dept):
            raise KeyError
        return self.s[dept]


Dcap = DCapAlst()
