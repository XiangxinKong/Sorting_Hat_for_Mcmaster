## @SALst.py
#  @Student Allocation List
#  @author Xiangxin Kong
#  @date 2/11 2019

from AALst import *
from DCapALst import *


#  @brief implement the allocation
class SALst:
    ## @brief constructor for SALst
    def __init__(self):
        self.s = {}

    ## @brief add a new student to the list
    #  @param macid of the students
    #  @param information about the student
    def add(self, macid, s_info):
        if self.elm(macid):
            raise KeyError
        self.s[macid] = s_info

    ## @brief remove a student from the list
    #  @param macid of the student
    def remove(self, macid):
        if not self.elm(macid):
            raise KeyError
        self.s.pop(macid)

    ## @brief check if the list contains certain student
    #  @param macid of the student
    #  @return boolean of the result
    def elm(self, macid):
        return self.s.__contains__(macid)

    ## @brief output the information about the student
    #  @param the macid of the student
    def info(self, macid):
        if not self.elm(macid):
            raise KeyError
        return self.s[macid]

    ## @brief sort the students in list by GPA with condition
    #  @param function that set the domain for sorting
    #  @return the sorted list with macid
    def sort(self, f=lambda x: True):
        sort_id = []
        v = self.s.copy()
        for c in self.s:
            if not f(self.s[c]):
                v.pop(c)
        for i in sorted(v, key=lambda x: v[x][3]):
            sort_id.append(i)
        sort_id.reverse()
        return sort_id

    ## @brief output the average gpa under condition f
    #  @param function that set the domain for average
    #  @return the average gpa
    def average(self, f=lambda x: True):
        v = self.s.copy()
        for c in self.s:
            if not f(self.s[c]):
                v.pop(c)
        if len(v) == 0:
            raise ValueError
        sum = 0
        for i in v:
            sum += v[i][3]
        return sum / len(v)

    ## @brief implement the allocation
    #  @details allocate the students with 4.0+ by free choice and gpa
    def allocate(self):
        try:
            #
            namels = self.sort(lambda x: x[3] >= 4.0 and x[4])
            for i in namels:
                self.s[i][4].start()
                dep = self.s[i][4].next()
                if Dcap.capacity(dep) > alloc.num_alloc(dep):
                    alloc.add_stdnt(dep, i)
                else:
                    dep = self.s[i][4].next()
                    if Dcap.capacity(dep) > alloc.num_alloc(dep):
                        alloc.add_stdnt(dep, i)
                    else:
                        alloc.add_stdnt(self.s[i][4].next(), i)
        except Exception as e:
            print(e)
            raise RuntimeError
