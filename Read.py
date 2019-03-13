## @DcapALst.py
#  @Allocation List
#  @author Xiangxin Kong
#  @date 2/11 2019

## @brief read the data from txt file
from DCapALst import *
from SALst import *

stdnt = SALst()


## @brief read the data from txt file
class Read:
    ## @brief load the student-data
    def load_stdnt_data(self, s):
        filelines = open(s, "r").readlines()
        for line in filelines:
            std = line.split(",")
            std[5] = std[5][2:]
            std[-2] = std[-2][:-1]
            std[-1] = std[-1][:-1]
            std = list(map(lambda x: x.strip(), std))
            id = std[0]
            seqls = std[5:-1]
            seqls = list(map(lambda x: getattr(DeptT, x), seqls))
            stdnt.add(
                id,
                SInfoT(std[1], std[2], 1, float(std[4]), SeqADT(seqls), bool(std[6])),
            )

    ## @brief load the department capacity data
    def load_dcap_data(self, s):
        filelines = open(s, "r").readlines()
        for line in filelines:
            dept = line.split()
            Dcap.add(getattr(DeptT, dept[0][:-1]), int(dept[1]))


temp = Read()
