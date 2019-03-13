from SeqADT import *
from DCapALst import *
from SALst import *
import pytest


class TestSeqADT:
    def setup_method(self):
        self.A = SeqADT([1, 2, 3])

    def test_next_return_value(self):
        one = self.A.next()
        two = self.A.next()
        assert one == 1 and two == 2

    def test_start_method(self):
        self.A.next()
        self.A.start()
        assert self.A.next() == 1

    def test_end(self):
        assert not self.A.end()

    def test_end_exception(self):
        with pytest.raises(StopIteration):
            self.A.next()
            self.A.next()
            self.A.next()
            self.A.next()


class TestDCapAlst:
    def setup_method(self):
        self.A = DCapAlst()

    def test_add(self):
        self.A.add(DeptT.software, 0)
        assert self.A.capacity(DeptT.software) == 0

    def test_repeated_add(self):
        with pytest.raises(KeyError):
            self.A.add(DeptT.software, 101)
            self.A.add(DeptT.software, 1)

    def test_elm(self):
        self.A.add(DeptT.software, 100)
        assert self.A.elm(DeptT.software) and (not self.A.elm(DeptT.civil))

    def test_remove(self):
        self.A.add(DeptT.software, 102)
        self.A.remove(DeptT.software)
        assert not self.A.elm(DeptT.software)

    def test_remove_exception(self):
        with pytest.raises(KeyError):
            self.A.remove(DeptT.mechanical)

    def test_capacity(self):
        self.A.add(DeptT.civil, 12)
        assert self.A.capacity(DeptT.civil) == 12

    def test_capacity_error(self):
        with pytest.raises(KeyError):
            self.A.capacity(DeptT.engphys)


class TestSALst:
    def setup_method(self):
        self.x = SInfoT(
            "Xiangxin",
            "Kong",
            GenT.male,
            10.0,
            SeqADT([DeptT.software, DeptT.chemical, DeptT.civil]),
            False,
        )
        y = SInfoT(
            "kexin",
            "liu",
            GenT.female,
            9.0,
            SeqADT([DeptT.materials, DeptT.chemical, DeptT.engphys]),
            False,
        )
        z = SInfoT(
            "Tianrui",
            "He",
            GenT.male,
            8.0,
            SeqADT([DeptT.materials, DeptT.chemical, DeptT.engphys]),
            True,
        )
        m = SInfoT(
            "Jason",
            "Lee",
            GenT.male,
            3.0,
            SeqADT([DeptT.materials, DeptT.materials, DeptT.engphys]),
            True,
        )
        self.ls = SALst()
        self.ls.__init__()
        self.ls.add("kongx9", self.x)
        self.ls.add("Xe67", m)
        self.ls.add("ke26", y)
        self.ls.add("He35", z)

    def test_add(self):
        assert self.ls.info("kongx9") == self.x

    def test_add_error(self):
        with pytest.raises(KeyError):
            self.ls.add("kongx9", self.x)

    def test_elm(self):
        assert self.ls.elm("kongx9") and not self.ls.elm("not exist")

    def test_remove(self):
        self.ls.remove("ke26")
        assert not self.ls.elm("ke26")

    def test_remove_error(self):
        with pytest.raises(KeyError):
            self.ls.remove("Not Exist")

    def test_average(self):
        assert self.ls.average() == pytest.approx(7.5, rel=0.001)

    def test_average_condition(self):
        assert self.ls.average(lambda x: x.gpa >= 4.0) == pytest.approx(9.0, rel=0.001)

    def test_average_zero_divition(self):
        with pytest.raises(ValueError):
            self.ls.average(lambda x: False)

    def test_sort(self):
        sl = self.ls.sort()
        assert sl[0] == "kongx9" and sl[1] == "ke26" and sl[2] == "He35"

    def test_sort_condition(self):
        s_l = self.ls.sort(lambda x: x.freechoice)
        assert s_l[0] == "He35" and s_l[1] == "Xe67"

    def test_sort_empty(self):
        sl = self.ls.sort(lambda x: False)
        assert len(sl) == 0

    def test_result_admission_order(self):
        Dcap.add(DeptT.civil, 11)
        Dcap.add(DeptT.software, 1)
        Dcap.add(DeptT.electrical, 12)
        Dcap.add(DeptT.chemical, 13)
        Dcap.add(DeptT.engphys, 14)
        Dcap.add(DeptT.materials, 15)
        Dcap.add(DeptT.mechanical, 16)
        self.ls.add(
            "Yui13",
            SInfoT(
                "Asuka",
                "Yui",
                GenT.female,
                7.0,
                SeqADT([DeptT.software, DeptT.chemical, DeptT.civil]),
                False,
            ),
        )
        self.ls.allocate()
        assert ("Yui13" in alloc.lst_alloc(DeptT.chemical)) and (
            "kongx9" in alloc.lst_alloc(DeptT.software)
        )  # check allocate by grade
        assert ("He35" in alloc.lst_alloc(DeptT.materials)) and not (
            "Ke35" in alloc.lst_alloc(DeptT.materials)
        )  # check freechoice
        assert not self.ls.elm("Xe26")  # gpa 4.0+
