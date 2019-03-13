## @AALst.py
#  @Allocation List
#  @author Xiangxin Kong
#  @date 2/11 2019

## @brief the final allocation result save here
from StdntAllocTypes import *


## @brief dictionary of allocation result
class AAlst:
    ## @brief Constructor for AAlst
    def __init__(self):
        self.s = {
            DeptT.software: [],
            DeptT.civil: [],
            DeptT.chemical: [],
            DeptT.electrical: [],
            DeptT.engphys: [],
            DeptT.mechanical: [],
            DeptT.materials: [],
        }

    ## @add new student to the dictionary
    #  @param Department name
    #  @param macid
    def add_stdnt(self, dept, name):
        self.s[dept].append(name)

    ## @brief output the allocation result
    #  @param name of the department
    #  @return students in that dept
    def lst_alloc(self, dept):
        return self.s[dept]

    ## @brief number of students in the dept
    #  @param name of the department
    #  @return number of students
    def num_alloc(self, dept):
        return len(self.s[dept])


alloc = AAlst()
alloc.__init__()
