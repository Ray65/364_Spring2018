#! /usr/bin/env python3.4
import os
import enum
import re
import random
from uuid import UUID
import operator

class Level(enum.Enum):
    freshman = "Freshman"
    sophomore = "Sophomore"
    junior = "Junior"
    senior = "Senior"


class Student():
    def __init__(self, ID, firstName, lastName, level):
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self.level = level

        if not isinstance(self.level, Level):
            raise TypeError("The argument must be an instance of the 'Level' Enum.")

    def __str__(self):
        #ret_str = ""
        id_exp = r'([0-9]{5}\-[0-9]{5})'
        if re.match(id_exp, str(self.ID)):
            lev = self.level
            ret_str = str(self.ID)+", "+str(self.firstName)+" "+str(self.lastName)+", "+str.capitalize(str(lev.name))
            return  ret_str
        else:
            raise TypeError("ID is not in XXXXX-XXXXX format")

class Circuit:

    def __init__(self, ID, resistors, capacitors, inductors, transistors):

        id_exp = r'([0-9]{5})'
        if re.match(id_exp, str(ID)):
            self.ID = ID
            if isinstance(transistors, list):
                trans_list = []
                not_trans_list = []
                if not transistors:
                    self.transistors = transistors
                else:
                    for elem in transistors:
                        if(elem[:1] == 'T'):
                            trans_list.append(elem)
                        else:
                            not_trans_list.append(elem)
                    self.transistors = trans_list
                    if not_trans_list:
                        raise ValueError("The transistors' list contain invalid components - "+str(not_trans_list))

            if isinstance(resistors, list):
                res_list = []
                not_res_list = []
                if not resistors:
                    self.resistors = resistors
                else:
                    for elem in resistors:
                        if(elem[:1] == 'R'):
                            res_list.append(elem)
                        else:
                            not_res_list.append(elem)
                    self.resistors = res_list
                    if not_res_list:
                        raise ValueError("The resistors' list contain invalid components - "+str(not_res_list))

            if isinstance(capacitors, list):
                cap_list = []
                not_cap_list = []
                if not capacitors:
                    self.capacitors = capacitors
                else:
                    for elem in capacitors:
                        if(elem[:1] == 'C'):
                            cap_list.append(elem)
                        else:
                            not_cap_list.append(elem)
                    self.capacitors = cap_list
                    if not_cap_list:
                        raise ValueError("The capacitors' list contain invalid components - "+str(not_cap_list))

            if isinstance(inductors, list):
                ind_list = []
                not_ind_list = []
                if not inductors:
                    self.inductors = inductors
                else:
                    for elem in inductors:
                        if(elem[:1] == 'L'):
                            ind_list.append(elem)
                        else:
                            not_ind_list.append(elem)
                    self.inductors = ind_list
                    if not_ind_list:
                        raise ValueError("The inductors' list contain invalid components - "+str(not_ind_list))
        else:
            raise TypeError("ID is not in XXXXX format")

    def __str__(self):
        res_len = len(self.resistors)
        ind_len = len(self.inductors)
        trans_len = len(self.transistors)
        cap_len = len(self.capacitors)
        str_rep = self.ID+": (R = "+'{:02}'.format(res_len)+", C = "+'{:02}'.format(cap_len)+", L = "+'{:02}'.format(ind_len)+", T = "+'{:02}'.format(trans_len)+")"
        return str_rep

    def getDetails(self):
        sort_res = sorted(self.resistors)
        sort_ind = sorted(self.inductors)
        sort_trans = sorted(self.transistors)
        sort_cap = sorted(self.capacitors)

        str_det_intrm = self.ID+": "+(', '.join(sort_res))+", "+(', '.join(sort_cap))+", "+(', '.join(sort_ind))+", "+(', '.join(sort_trans))
        str_det = str_det_intrm.strip()
        return str_det

    #Operator Overloading

    #Membership Check
    def __contains__(self, item):
        if isinstance(item, str):
            if item[:1] == 'R':
                if item in self.resistors:
                    return True
                else:
                    return False

            elif item[:1] == 'L':
                if item in self.inductors:
                    return True
                else:
                    return False

            elif item[:1] == 'C':
                if item in self.capacitors:
                    return True
                else:
                    return False

            elif item[:1] == 'T':
                if item in self.transistors:
                    return True
                else:
                    return False

            else:
                raise ValueError("Invalid component type.")

        else:
            raise TypeError("Item must be of type string.")

    #Adding of (Circuit + component) & (Circuit1 + Circuit2)
    def __add__(self, other):
        #if isinstance(other, self.resistors) or isinstance(other, self.inductors) or isinstance(other, self.transistors) or isinstance(other, self.capacitors):
        if isinstance(other, str):
            #if (other[:1] == 'R') or (other[:1] == 'L') or (other[:1] == 'T') or (other[:1] == 'C'):
            if (other[:1] == 'R'):
                if other not in self.resistors:
                    self.resistors.append(other)
                    return self
                else:
                    return self

            elif (other[:1] == 'L'):
                if other not in self.inductors:
                    self.inductors.append(other)
                    return self
                else:
                    return self

            elif (other[:1] == 'C'):
                if other not in self.capacitors:
                    self.capacitors.append(other)
                    return self
                else:
                    return self

            elif (other[:1] == 'T'):
                if other not in self.transistors:
                    self.transistors.append(other)
                    return self
                else:
                    return self

            else:
                raise ValueError("Invalid component type.")

        elif isinstance(other, Circuit):
            rnums = range(10000, 100000)
            r_id = random.sample(rnums, 1)
            new_res_list = list(set(self.resistors + other.resistors))
            new_cap_list = list(set(self.capacitors + other.capacitors))
            new_ind_list = list(set(self.inductors + other.inductors))
            new_trans_list = list(set(self.transistors + other.transistors))

            new_cir = Circuit(r_id[0], new_res_list, new_cap_list, new_ind_list, new_trans_list)

            return new_cir

        else:
            raise TypeError("Other must be of type str or Circuit.")

    #Commutative adding of Circuit + component
    def __radd__(self, other):
        if isinstance(other, str):
            if (other[:1] == 'R'):
                if other not in self.resistors:
                    self.resistors.append(other)
                    return self
                else:
                    return self

            elif (other[:1] == 'L'):
                if other not in self.inductors:
                    self.inductors.append(other)
                    return self
                else:
                    return self

            elif (other[:1] == 'C'):
                if other not in self.capacitors:
                    self.capacitors.append(other)
                    return self
                else:
                    return self

            elif (other[:1] == 'T'):
                if other not in self.transistors:
                    self.transistors.append(other)
                    return self
                else:
                    return self

            else:
                raise ValueError("Invalid component type.")

        else:
            raise TypeError("Component must be of type str.")

    #Removing component from circuit
    def __sub__(self, other):
        if isinstance(other, str):
            if (other[:1] == 'R'):
                if other in self.resistors:
                    self.resistors.remove(other)
                    return self
                else:
                    return self

            elif (other[:1] == 'L'):
                if other in self.inductors:
                    self.inductors.remove(other)
                    return self
                else:
                    return self

            elif (other[:1] == 'C'):
                if other in self.capacitors:
                    self.capacitors.remove(other)
                    return self
                else:
                    return self

            elif (other[:1] == 'T'):
                if other in self.transistors:
                    self.transistors.remove(other)
                    return self
                else:
                    return self

            else:
                raise ValueError("Invalid component type.")

        else:
            raise TypeError("Component must be of type str.")

class Project:

    def __init__(self, ID, participants, circuits):
        self.ID = ID
        if participants:
            for elem in participants:
                if isinstance(elem, Student):
                    self.participants = participants
                else:
                    raise TypeError("Participant must be of type student.")
        else:
            raise ValueError("Participants list is empty.")

        if circuits:
            for elem in circuits:
                if isinstance(elem, Circuit):
                    self.circuits = circuits
                else:
                    raise TypeError("Circuits element must be of type Circuit.")
        else:
            raise ValueError("Circuits list is empty.")

    def __str__(self):
        part_len = len(self.participants)
        cir_len = len(self.circuits)
        str_rep = self.ID+": "+'{:02}'.format(cir_len)+" Circuits, "+'{:02}'.format(part_len)+" Participants"
        return str_rep


    def getDetails(self):
        sorted_part = sorted(self.participants, key=operator.attrgetter('ID'))
        sorted_cir = sorted(self.circuits, key=operator.attrgetter('ID'))
        part_str = ""
        cir_str = ""
        for part in sorted_part:
            part_str += part.__str__()+"\n"
        for cir in sorted_cir:
            cir_str += cir.getDetails()+"\n"
        fin_str = "\n"+self.ID+"\n"+"Participants:\n"+part_str+"\nCircuits:\n"+cir_str+"\n"

        return fin_str


    def __contains__(self, item):
        if isinstance(item, str):
            for cir in self.circuits:
                if item[:1] == 'R':
                    if item in cir.resistors:
                        return True
                    else:
                        return False

                elif item[:1] == 'L':
                    if item in cir.inductors:
                        return True
                    else:
                        return False

                elif item[:1] == 'C':
                    if item in cir.capacitors:
                        return True
                    else:
                        return False

                elif item[:1] == 'T':
                    if item in cir.transistors:
                        return True
                    else:
                        return False

                else:
                    raise ValueError("Invalid component type.")

        elif isinstance(item, Circuit):
            for circuit in self.circuits:
                if item.ID == circuit.ID:
                    return True

            return False

        elif isinstance(item, Student):
            for part in self.participants:
                if item.ID == part.ID:
                    return True

            return False
        else:
            raise TypeError("Item not of appropriate type.")


    def __add__(self, other):
        if isinstance(other, Circuit):
            if other not in self.circuits:
                self.circuits.append(other)
                return self
            else:
                return self

        elif isinstance(other, Student):
            if other not in self.participants:
                self.participants.append(other)
                return self
            else:
                return self

        else:
            raise TypeError("Other must be type Circuit or Student.")

    def __sub__(self, other):
        if isinstance(other, Circuit):
            if other in self.circuits:
                self.circuits.remove(other)
                return self
            else:
                return self

        elif isinstance(other, Student):
            if other in self.participants:
                self.participants.remove(other)
                return self
            else:
                return self

        else:
            raise TypeError("Other must be of type Circuit or Student.")

class Capstone(Project):

    def __init__(self, ID, participants, circuits):
        Project.__init__(self, ID, participants, circuits)
        for part in self.participants:
            #print(part.level)
            #if part.level.value != "Senior":
            if part.level != Level.senior:

                raise ValueError("All participants must be Seniors.")

    def __add__(self, other):
        Project.__add__(self, other)
        if isinstance(other, Student):
            #if other.level.value != "Senior":
            if other.level != Level.senior:
                raise ValueError("All students must be seniors.")




    #print(Level.freshman.value)
    s = Student("45678-89476", "John", "Smith", Level.senior)
    s2 = Student("12345-12345", "Bob", "Givan", Level.junior)
    s3 = Student("09872-23452", "George", "Brown", Level.sophomore)
    s4 = Student("99999-99999", "Aishwarya", "Ray", Level.senior)
    #print(s.ret_string())
    res = ["R456.87", "R34.33", "R346.98", "R324"]
    cap = ["C4876", "C84756",]
    ind = ["L987", "L8973"]
    trn = ["T4"]
    res2 = ["R56", "R23976.45", "R324"]
    ind2 = ["L7", "L897"]
    c = Circuit("12345", res, cap, ind, trn)
    n = Circuit("45678", res2, cap, ind2, trn)
    #print(c.getDetails())
    c-"R45"
    "T56" + c
    #print(c.resistors)
    #print(c.transistors)
    #print(c.ret_string())

    nc = c + n
    #print(nc.resistors)
    #print(nc.capacitors)
    #print(nc.inductors)
    #print(nc.transistors)
    #print(nc.ID)

    cir_list = [c]
    stu_list = [s]
    #print(s.__str__())
    #for i in stu_list:
    #    print(i.__str__())
    proj = Project("123", stu_list, cir_list)
    #print(proj.getDetails())
    #print("R324" in proj)
    proj + n
    #proj + s3
    #proj - s
    proj - c
    #print(proj.getDetails())

    caps = Capstone("12345", stu_list, cir_list)
    #print(caps+s4)



