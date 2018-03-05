#! /usr/bin/env python3.4
import re
from uuid import UUID

#Helper function to make dictionary with list as values
def _make_dictionary(key, val, dictionary):
    if key not in dictionary:
        elem_list = []
        elem_list.append(val)
        dictionary[key] = elem_list
    else:
        dictionary[key].append(val)
    return dictionary

#Helper function to parse Employees.txt file
def _parse_employees():
    emp = {}
    editted_line_wo_id = ""
    #Parsing name
    name_exp1 = r'((?P<fname>[\w.-]+)\s(?P<lname>[\w.-]+))'
    name_exp2 = r'((?P<lname>[\w.-]+)\,\s(?P<fname>[\w.-]+))'

    #Parsing ID
    ID_exp_short = r'((\{?[a-fA-F0-9]{8}\-?[a-fA-F0-9]{4}\-?[a-fA-F0-9]{4}\-?[a-fA-F0-9]{4}\-?[a-fA-F0-9]{12}\}?))'

    #Parsing phone number
    phone_exp_short = r'((\(?(?P<f3>[0-9]{3})\)?\s?\-?(?P<s3>[0-9]{3})\-?(?P<l4>[0-9]{4})))'

    #Parsing state
    state_exp1 = r'([a-zA-Z]+\b)'
    state_exp2 = r'((?P<state_name1>[\w.-]+)\s(?P<state_name2>[\w.-]+))'
    #Making dictionary with name as key and value as parsed values
    with open('Employees.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if re.search(name_exp2, line):
            #name1 = re.search(name_exp2, line).group(1)
            m1 = re.match(name_exp2, line)
            id_flag = 0
            name1 = m1.group("fname")+" "+m1.group("lname")
            editted_line_wo_name = str(re.sub(name_exp2, ' ', str(line)))
            editted_line_wo_id_name = str(re.sub(ID_exp_short, ' ', str(editted_line_wo_name)))
            #State
            if re.search(state_exp2, editted_line_wo_id_name):
                m5 = re.search(state_exp2, editted_line_wo_id_name)
                state = str(m5.group(1))
                #print(name1+"   "+state)
                emp = _make_dictionary(name1, state, emp)
            elif re.search(state_exp1, editted_line_wo_id_name):
                m5 = re.search(state_exp1, editted_line_wo_id_name)
                state = str(m5.group(1))
                #print(state+"   "+name1)
                #print(name1+"   "+state)
                emp = _make_dictionary(name1, state, emp)

            #ID
            if re.search(ID_exp_short, line):
                m2 = re.search(ID_exp_short, line)
                emp = _make_dictionary(name1, str(UUID(m2.group(1))), emp)
                id_flag = 1
                editted_line_wo_id = str(re.sub(ID_exp_short, ' ', str(line)))
                #print(editted_line_wo_id)


            #Phone Number
            if id_flag == 1:
                if re.search(phone_exp_short, editted_line_wo_id):
                    m4 = re.search(phone_exp_short, editted_line_wo_id)
                    num = "("+m4.group("f3")+") "+m4.group("s3")+"-"+m4.group("l4")
                    #print(num)
                    emp = _make_dictionary(name1, num, emp)


            elif id_flag == 0:
                if re.search(phone_exp_short, line):
                    m4 = re.search(phone_exp_short, line)
                    num = "("+m4.group("f3")+") "+m4.group("s3")+"-"+m4.group("l4")
                    #print(num)
                    emp = _make_dictionary(name1, num, emp)


            else:
                continue

        #Case when name is of format: <FirstName> <LastName>
        elif re.search(name_exp1, line):
            m3 = re.match(name_exp1, line)
            id_flag = 0
            #print(m3)
            editted_line_wo_name = str(re.sub(name_exp1, ' ', str(line), 1))
            editted_line_wo_id_name = str(re.sub(ID_exp_short, ' ', str(editted_line_wo_name)))

            #State
            if re.search(state_exp2, editted_line_wo_id_name):
                m5 = re.search(state_exp2, editted_line_wo_id_name)
                state = str(m5.group(1))
                #print(state+"   "+m3.group(1))
                emp = _make_dictionary(m3.group(1), state, emp)

            elif re.search(state_exp1, editted_line_wo_id_name):
                m5 = re.search(state_exp1, editted_line_wo_id_name)
                state = str(m5.group(1))
                emp = _make_dictionary(m3.group(1), state, emp)



            if re.search(ID_exp_short, line):
                m2 = re.search(ID_exp_short, line)
                emp = _make_dictionary(m3.group(1), str(UUID(m2.group(1))), emp)
                id_flag = 1
                editted_line_wo_id = str(re.sub(ID_exp_short, ' ', str(line)))
                #print(editted_line_wo_id)
            if id_flag == 1:
                if re.search(phone_exp_short, editted_line_wo_id):
                    m4 = re.search(phone_exp_short, editted_line_wo_id)
                    num = "("+m4.group("f3")+") "+m4.group("s3")+"-"+m4.group("l4")
                    #print(num)
                    emp = _make_dictionary(m3.group(1), num, emp)

            elif id_flag == 0:
                if re.search(phone_exp_short, line):
                    m4 = re.search(phone_exp_short, line)
                    num = "("+m4.group("f3")+") "+m4.group("s3")+"-"+m4.group("l4")
                    #print(num)
                    emp = _make_dictionary(m3.group(1), num, emp)



            else:
                continue
        else:
            continue
            #print(m3.group(1))
    #print(line)
    #print(emp)
    return emp


#Part1 Task1
def getUrlParts(url):
    output = re.split(',|/|\?', url)
    output_tuple = tuple(output[2:5])
    return output_tuple

#Part1 Task2
def getQueryParameters(url):
    output = re.split(',|/|\?', url)
    param = []
    #output_tuple = tuple(output[2:5])
    queries = output[5].split("&")
    for query in queries:
        param_list = query.split("=")
        param_tuple = tuple(param_list)
        param.append(param_tuple)
    return param

#Part1 Task3
def getSpecial(sentence, letter):

    intrm_list = []
    exp = re.match(r'(?P<ltr>[\w.-]+)', letter)
    #print(exp.group("ltr"))
    expr2 = re.compile(r'\b\w+', re.I)
    word_list = re.findall(expr2, sentence)
    pat = "^"+letter+"|"+letter+"$"
    pat2 = "^"+letter+".+"+letter+"$"

    for word in word_list:
        if re.search(pat,word,re.IGNORECASE):
            if re.search(pat2,word,re.IGNORECASE):
                continue
            else:
                intrm_list.append(word)
        else:
            continue
    return intrm_list


#Part1 Task4
def getRealMAC(sentence):

    patt_colon= r'(([a-fA-F0-9]{2}\:){5}[a-fA-F0-9]{2})'
    patt_hyphen= r'(([a-fA-F0-9]{2}\-){5}[a-fA-F0-9]{2})'

    if re.search(patt_hyphen, sentence):

        m = re.search(patt_hyphen, sentence)
        return (m.group(1))
    elif re.search(patt_colon, sentence):
        m = re.search(patt_colon, sentence)
        return (m.group(1))
    else:
        return None

#Part2 Task1
def getRejectedEntries():
    employees = {}
    employees = _parse_employees()
    reject_list = []
    with open('Employees.txt', 'r') as f:
        lines = f.readlines()
    #Parsing name
    name_exp1 = r'((?P<fname>[\w.-]+)\s(?P<lname>[\w.-]+))'
    name_exp2 = r'((?P<lname>[\w.-]+)\,\s(?P<fname>[\w.-]+))'
    for line in lines:
        if re.search(name_exp2, line):
            k2 = re.search(name_exp2, line)
            name2 = k2.group("fname")+" "+k2.group("lname")
            if name2 not in employees:
                reject_list.append(name2)
            #print(name2)
        elif re.search(name_exp1, line):
            k1 = str(re.search(name_exp1, line).group(1))
            if k1 not in employees:
                reject_list.append(k1)
            #print(k1)
    sorted_rejects = sorted(reject_list)
    #print(len(employees))
    return sorted_rejects

#Part2 task2
def getEmployeesWithIDs():
    employees = {}
    emp_id = {}

    employees = _parse_employees()
    #Parsing ID
    ID_exp_short = r'((\{?[a-fA-F0-9]{8}\-?[a-fA-F0-9]{4}\-?[a-fA-F0-9]{4}\-?[a-fA-F0-9]{4}\-?[a-fA-F0-9]{12}\}?))'
    with open('Employees.txt', 'r') as f:
        lines = f.readlines()
    for name, detail_list in employees.items():
        for elem in detail_list:
            if re.search(ID_exp_short, elem):
                emp_id[name] = elem
            else:
                continue
    return emp_id

#Part2 task3
def getEmployeesWithoutIDs():
    employees = {}
    emp_list = []

    employees = _parse_employees()
    #Parsing ID
    ID_exp_short = r'((\{?[a-fA-F0-9]{8}\-?[a-fA-F0-9]{4}\-?[a-fA-F0-9]{4}\-?[a-fA-F0-9]{4}\-?[a-fA-F0-9]{12}\}?))'
    with open('Employees.txt', 'r') as f:
        lines = f.readlines()
    for name, detail_list in employees.items():
        for elem in detail_list:
            if re.search(ID_exp_short, elem):
                continue
            else:
                emp_list.append(name)
    sorted_emp_list = sorted(emp_list)
    return sorted_emp_list

#Part2 Task4
def getEmployeesWithPhones():
    employees = {}
    emp_phone = {}

    employees = _parse_employees()
    #Parsing phone number
    phone_exp_short = r'((\(?(?P<f3>[0-9]{3})\)?\s?\-?(?P<s3>[0-9]{3})\-?(?P<l4>[0-9]{4})))'

    with open('Employees.txt', 'r') as f:
        lines = f.readlines()
    for name, detail_list in employees.items():
        for elem in detail_list:
            if re.search(phone_exp_short, elem):
                emp_phone[name] = elem
            else:
                continue
    return emp_phone

#Part2 Task5
def getEmployeesWithStates():
    employees = {}
    emp_states = {}

    employees = _parse_employees()
    #Parsing state
    state_exp1 = r'([a-zA-Z]+\b)'
    state_exp2 = r'((?P<state_name1>[\w.-]+)\s(?P<state_name2>[\w.-]+))'

    with open('Employees.txt', 'r') as f:
        lines = f.readlines()
    for name, detail_list in employees.items():
        for elem in detail_list:
            if re.search(state_exp2, elem):
                if re.search(r'(\d)', elem):
                    continue
                else:
                    emp_states[name] = elem
            elif re.search(state_exp1, elem):
                if re.search(r'(\d)', elem):
                    continue
                else:
                    emp_states[name] = elem
            else:
                continue
    #print(len(emp_states))
    return emp_states

#Part2 Task6
def getCompleteEntries():
    employees = {}
    emp_complete = {}

    employees = _parse_employees()
    for name, detail_list in employees.items():
        emp_details = []
        if (len(detail_list) == 3):
            emp_details.append(detail_list[1])
            emp_details.append(detail_list[2])
            emp_details.append(detail_list[0])
            #print(name)
            emp_tuple = tuple(emp_details)
            emp_complete[name] = emp_tuple
        else:
            continue
    #print(len(emp_complete))
    return emp_complete


if __name__ == "__main__":
    #print(getUrlParts("http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"))
    url1 = "http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"
    url2 = "http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here"
    s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
    sent = "The wehfhqwe MAC address d4:5C:5b:6E:69:5D wiefiwh qhhbhbhbh ."
    #print(getSpecial(s, "t"))
    #print(getRealMAC(sent))
    #getRejectedEntries()
    #print(_parse_employees())
    #print(getRejectedEntries())
    #getRejectedEntries()
    #print(getEmployeesWithIDs())
    #print(getEmployeesWithoutIDs())
    #print(getEmployeesWithPhones())
    #print(getEmployeesWithStates())
    print(getCompleteEntries())
