## @StdntAllocTypes.py
#  @title students Allocation Types
#  @author Xiangxin Kong
#  @date 2/11 2019

## @brief define the nessary types
from SeqADT import *
from typing import NamedTuple


## @brief This class repersents male and female type
class GenClass:
    male = 0
    female = 1


## @brief This class repersents Department type
class DeptClass:
    civil = 0
    chemical = 1
    electrical = 2
    mechanical = 3
    software = 4
    materials = 5
    engphys = 6


GenT = GenClass()
DeptT = DeptClass()
## @brief template for student information
SInfoT = NamedTuple(
    "SInfo",
    fname=str,
    lname=str,
    gender=int,
    gpa=float,
    choices=SeqADT,
    freechoice=bool,
)
