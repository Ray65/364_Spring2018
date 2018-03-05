#! /usr/bin/env python3.4

#Helper function to make dictionary of lists
def _make_dictionary(key, val, dictionary):
    if key not in dictionary:
        elem_list = []
        elem_list.append(val)
        dictionary[key] = elem_list
    else:
        dictionary[key].append(val)
    return dictionary

def _make_dictionary_set(key, val, dictionary):
    if key not in dictionary:
        elem_set = set()
        elem_set.add(val)
        dictionary[key] = elem_set
    else:
        dictionary[key].add(val)
    return dictionary

def _make_student_dictionary():
    #Building dictionary for students
    with open("students.txt", "r") as f:
        lines = f.readlines()[2:]
    stu = {}
    no_lines = len(lines)
    for i in range(no_lines):
        elements = lines[i].split("|")
        name = elements[0].strip()
        sid = elements[1].strip()
        stu = _make_dictionary(sid, name, stu)
    return stu

def _make_circuits_dictionary():
    #Building dictionary of project ID and circuits
    with open("projects.txt", "r") as f:
        lines = f.readlines()
    no_lines = len(lines)
    items = []
    circuits = {}
    for i in range(2,no_lines):
        items.append(lines[i].strip())
    no_items = len(items)
    for j in range(no_items):
        elements = items[j].split("         ")
        circuits = _make_dictionary(elements[1], elements[0], circuits)
    return circuits

def _no_of_lines_in_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    no_lines = len(lines)
    return no_lines


#Prob 1
def getComponentCountByProject(projectID):
    with open("projects.txt", "r") as f:
        lines = f.readlines()

    no_lines = len(lines)
    items = []
    circuits = {}
    sum = 0
    transistors = set()
    inductors = set()
    resistors = set()
    capacitors = set()
    t = tuple()
    for i in range(2,no_lines):
        items.append(lines[i].strip())
    no_items = len(items)
    for j in range(no_items):
        elements = items[j].split("         ")
        circuits = _make_dictionary(elements[1], elements[0], circuits)

    #print(circuits)
    if projectID not in circuits:
        return None
    else:
        no_circuits = len(circuits[projectID])
        project_list = circuits[projectID]

        #print("no_circuits:")
        #print(no_circuits)
        for k in range(no_circuits):
            circuit_num = project_list[k]
            path = "Circuits/circuit_"+circuit_num+".txt"
            with open(path, "r") as file:
                file_lines = file.readlines()
                elem_line = file_lines[4]
                parts = elem_line.split(", ")
                no_parts = len(parts)
                for l in range(no_parts):
                    elem = parts[l]
                    if elem[0] == 'T':
                        transistors.add(elem)
                    elif elem[0] == 'R':
                        resistors.add(elem)
                    elif elem[0] == 'L':
                        inductors.add(elem)
                    elif elem[0] == 'C':
                        capacitors.add(elem)
                    else:
                        continue
        no_trans = len(transistors)
        no_resistors = len(resistors)
        no_inductors = len(inductors)
        no_caps = len(capacitors)
        t = (no_resistors, no_inductors, no_caps, no_trans)
        print(t)
        #print(circuits)
        return t


#Prob 2
def getComponentCountByStudent(studentName):
    import glob
    with open("students.txt", "r") as f:
        lines = f.readlines()[2:]
    #stunames = []
    #stuids = []
    transistors = set()
    inductors = set()
    resistors = set()
    capacitors = set()
    searchstu = []
    searchstu.append(studentName)
    t = tuple()
    stu = {}
    req_id = ""
    no_lines = len(lines)
    for i in range(no_lines):
        elements = lines[i].split("|")
        name = elements[0].strip()
        sid = elements[1].strip()
        stu = _make_dictionary(sid, name, stu)
        #stunames.append(name)
        #stuids.append(sid)
    #print(stu)
    if searchstu not in stu.values():
        return None

    for stuid, stuname in stu.items():
        if stuname[0] == studentName:
            #print(stuid)
            req_id = stuid
            circuit_files = glob.glob("Circuits/*")
            for file in circuit_files:
                #filename = "Circuits/"+file+".txt"
                with open(file, "r") as f:
                    flines = f.readlines()
                    line = flines[1]
                    elem_line = flines[4]
                    ppl = line.split(", ")
                    parts = elem_line.split(", ")
                    no_ppl = len(ppl)
                    for p in range(no_ppl):
                        if ppl[p] == req_id:
                            no_parts = len(parts)
                            for l in range(no_parts):
                                elem = parts[l]
                                if elem[0] == 'T':
                                    transistors.add(elem)
                                elif elem[0] == 'R':
                                    resistors.add(elem)
                                elif elem[0] == 'L':
                                    inductors.add(elem)
                                elif elem[0] == 'C':
                                    capacitors.add(elem)
                                else:
                                    continue
            no_trans = len(transistors)
            no_resistors = len(resistors)
            no_inductors = len(inductors)
            no_caps = len(capacitors)
            t = (no_resistors, no_inductors, no_caps, no_trans)
            #print(t)
            return t

#Prob 3
def getParticipationByStudent(studentName):
    import glob
    #Building dictionary with students
    with open("students.txt", "r") as f:
        lines = f.readlines()[2:]
    searchstu = []
    searchstu.append(studentName)
    stu = {}
    req_id = ""
    req_ckt = ""
    req_proj = ""
    participated_ckts = []
    participated_projects = set()
    #participated_projects = () //How to declare empty set????????????
    no_lines = len(lines)
    for i in range(no_lines):
        elements = lines[i].split("|")
        name = elements[0].strip()
        sid = elements[1].strip()
        stu = _make_dictionary(sid, name, stu)

    #Return "None" if reqd student doesn't exist
    if searchstu not in stu.values():
            return None

    for stuid, stuname in stu.items():
        if stuname[0] == studentName:
            #print(stuid)
            req_id = stuid
            circuit_files = glob.glob("Circuits/*")
            for file in circuit_files:
                #filename = "Circuits/"+file+".txt"
                with open(file, "r") as f:
                    flines = f.readlines()
                line = flines[1]
                #elem_line = flines[4]
                ppl = line.split(", ")
                #parts = elem_line.split(", ")
                no_ppl = len(ppl)
                for p in range(no_ppl):
                    if ppl[p] == req_id:
                        #req_ckt = file
                        cktname1 = file.split("_")
                        cktname2 = cktname1[1].split(".")
                        req_ckt = cktname2[0]
                        participated_ckts.append(req_ckt)
    no_participated_ckts = len(participated_ckts)

    #Building dictionary of projects
    with open("projects.txt", "r") as f:
        lines = f.readlines()[2:]
    no_lines = len(lines)
    items = []
    circuits = {}
    for i in range(no_lines):
        items.append(lines[i].strip())
    no_items = len(items)
    for j in range(no_items):
        elements = items[j].split("         ")
        circuits = _make_dictionary(elements[1], elements[0], circuits)

    #Checking for required match
    for projid, ckts in circuits.items():
        ckt_list = ckts
        ckt_list_len = len(ckt_list)
        for k in range(ckt_list_len):
            for m in range(no_participated_ckts):
                if ckt_list[k] == participated_ckts[m]:
                    req_proj = projid
                    participated_projects.add(req_proj)
                    #print(req_proj)
                else:
                    continue

    #print(participated_projects)
    #print(circuits)
    #print(participated_ckts)
    return participated_projects

#Prob 4
def getParticipationByProject(projectID):
    import glob
    mainset = set()
    with open("projects.txt", "r") as f:
        lines = f.readlines()[2:]

    no_lines = len(lines)
    items = []
    circuits = {}
    for i in range(no_lines):
        items.append(lines[i].strip())
    no_items = len(items)
    for j in range(no_items):
        elements = items[j].split("         ")
        circuits = _make_dictionary(elements[1], elements[0], circuits)
    if projectID not in circuits:
        return None
    else:
        no_circuits = len(circuits[projectID])
        project_list = circuits[projectID]

        #Building dictionary for students
        with open("students.txt", "r") as f:
            lines = f.readlines()[2:]
        stu = {}
        no_lines = len(lines)
        for i in range(no_lines):
            elements = lines[i].split("|")
            name = elements[0].strip()
            sid = elements[1].strip()
            stu = _make_dictionary(sid, name, stu)
        #print(stu)
        for k in range(no_circuits):
            circuit_num = project_list[k]
            path = "Circuits/circuit_"+circuit_num+".txt"
            with open(path, "r") as file:
                file_lines = file.readlines()
            participant_line = file_lines[1].strip()
            participants = participant_line.split(", ")
            no_participants = len(participants)
            #print(participants)
            req_stu_name = set()
            for n in range(no_participants):
                for stuid, stuname in stu.items():
                    if stuid == participants[n]:
                        req_stu_name.add(stuname[0])
                        mainset.update(req_stu_name)
                    else:
                        continue
        #print(mainset)
        return mainset

#Prob 5
def getProjectByComponent(components):
    import glob
    #Building dictionary of project ID and circuits
    """with open("projects.txt", "r") as f:
        lines = f.readlines()


    no_lines = len(lines)
    items = []
    circuits = {}
    for i in range(2,no_lines):
        items.append(lines[i].strip())
    no_items = len(items)
    for j in range(no_items):
        elements = items[j].split("         ")
        circuits = _make_dictionary(elements[1], elements[0], circuits)"""
    circuits = _make_circuits_dictionary()
    project_set_dictionary = {}
    components_list = list(components)
    no_of_components = len(components_list)
    req_project = ""
    #main_project_set = set()
    circuit_files = glob.glob("Circuits/*")
    for file in circuit_files:
        #filename = "Circuits/"+file+".txt"
        with open(file, "r") as f:
            flines = f.readlines()
        component_line = flines[4].strip()
        proj_comps = component_line.split(", ")
        #print("Project components:")
        #print(proj_comps)
        no_comp_line = len(proj_comps)
        #components is a set proj_comps is a list
        for i in range(no_comp_line):
            for j in range(no_of_components):
                if proj_comps[i] == components_list[j]:
                    circuit_fname = file
                    interim_circuit_fname1 = circuit_fname.split("_")
                    interim_circuit_fname2 = interim_circuit_fname1[1].split(".")
                    circuit_name = interim_circuit_fname2[0]
                    #print("Circuit filename:  "+circuit_fname)
                    #print(proj_comps[i]+"  "+components_list[j])
                    for projid, ckts in circuits.items():
                        ckt_list = ckts
                        ckt_list_len = len(ckt_list)
                        #print(ckt_list)
                        for k in range(ckt_list_len):
                            if ckt_list[k] == circuit_name:
                                #print("in if")
                                req_project = projid
                                project_set_dictionary = _make_dictionary_set(proj_comps[i], req_project, project_set_dictionary)
                                #main_project_set.add(req_project)
                                #print(projid)
    #print(pro)
    return project_set_dictionary

#Prob 6
def getStudentByComponent(components):
    import glob

    #Building dictionary for students
    """with open("students.txt", "r") as f:
        lines = f.readlines()[2:]
    stu = {}
    no_lines = len(lines)
    for i in range(no_lines):
        elements = lines[i].split("|")
        name = elements[0].strip()
        sid = elements[1].strip()
        stu = _make_dictionary(sid, name, stu) """
    stu = _make_student_dictionary()
    #Further component manipulation
    components_list = list(components)
    no_of_components = len(components_list)
    req_project = ""
    student_set_dictionary = {}
    circuit_files = glob.glob("Circuits/*")
    for file in circuit_files:
        #filename = "Circuits/"+file+".txt"
        with open(file, "r") as f:
            flines = f.readlines()
        component_line = flines[4].strip()
        proj_comps = component_line.split(", ")
        #print("Project components:")
        #print(proj_comps)
        no_comp_line = len(proj_comps)
        req_stu_name = ""
        #components is a set proj_comps is a list
        for i in range(no_comp_line):
            for j in range(no_of_components):
                if proj_comps[i] == components_list[j]:
                    #circuit_fname = file
                    participant_line = flines[1].strip()
                    participants = participant_line.split(", ")
                    no_of_participants = len(participants)
                    for k in range(no_of_participants):
                        for stuid, stuname in stu.items():
                            if stuid == participants[k]:
                                req_stu_name = stuname[0]
                                student_set_dictionary = _make_dictionary_set(proj_comps[i], req_stu_name, student_set_dictionary)
    return student_set_dictionary

#Prob 7
def getComponentsByStudents(studentNames):
    import glob
    stu = {}
    stu = _make_student_dictionary()
    req_stuid = ""
    main_component_dictionary = {}
    studentNames_list = list(studentNames)
    no_of_studs = len(studentNames_list)
    #print(studentNames_list)
    for stuid, stuname in stu.items():
        for i in range(no_of_studs):
            if studentNames_list[i] == stuname[0]:
                req_stuid = stuid
                #print(studentNames_list[i])
                circuit_files = glob.glob("Circuits/*")
                for file in circuit_files:
                    #filename = "Circuits/"+file+".txt"
                    with open(file, "r") as f:
                        flines = f.readlines()
                        participant_line = flines[1].strip()
                        participants = participant_line.split(", ")
                        no_of_participants = len(participants)
                        for j in range(no_of_participants):
                            if participants[j] == req_stuid:
                                used_comp_line = flines[4].strip()
                                #print(used_comp_line)
                                #print(participants[j])
                                used_comps = used_comp_line.split(", ")
                                #print(used_comps)
                                no_of_usedcomps = len(used_comps)
                                #print(studentNames_list[i])
                                for k in range(no_of_usedcomps):
                                    main_component_dictionary = _make_dictionary_set(studentNames_list[i], used_comps[k], main_component_dictionary)
    #print(main_component_dictionary)
    return main_component_dictionary

#Prob 8
def getCommonByProject(projectID1, projectID2):
    import glob
    circuits = {}
    circuits = _make_circuits_dictionary()
    if projectID1 not in circuits or projectID2 not in circuits:
        return None
    else:
        ckt_list1 = circuits[projectID1]
        ckt_list2 = circuits[projectID2]
        req_ckt = ""
        #print(ckt_list1)
        #print(ckt_list2)
        ckt_count1 = len(ckt_list1)
        ckt_count2 = len(ckt_list2)
        components_set1 = set()
        components_set2 = set()
        main_components_set1 = set()
        main_components_set2 = set()
        #components_list1 = []
        #components_list2 = []
        components_intersect_list = []
        components_intersect_set = set()
        for i in range(ckt_count1):
            path1 = "Circuits/circuit_"+ckt_list1[i]+".txt"
            with open(path1, "r") as f:
                flines = f.readlines()
            components_line1 = flines[4].strip()
            components1 = components_line1.split(", ")
            components_set1 = set(components1)
            main_components_set1.update(components_set1)
        #print(main_components_set1)
            #components_list1 = list(components_set1)
        for j in range(ckt_count2):
            path2 = "Circuits/circuit_"+ckt_list2[j]+".txt"
            with open(path2, "r") as f:
                flines = f.readlines()
            components_line2 = flines[4].strip()
            components2 = components_line2.split(", ")
            #print(components2)
            components_set2 = set(components2)
            main_components_set2.update(components_set2)
        #print(main_components_set2)
            #print(components_set2)

        components_intersect_set = main_components_set2.intersection(main_components_set1)
        #print(components_intersect_set)
        components_intersect_list = list(components_intersect_set)
        components_intersect_list.sort()
        #print(components_intersect_list)


        return components_intersect_list

#Prob 9
def getCommonByStudent(studentName1, studentName2):
    import glob
    stu = {}
    stu = _make_student_dictionary()
    req_stuid1 = ""
    req_stuid2 = ""
    components_set = set()
    components_list = []
    flag1 = 0
    flag2 = 0
    main_student_set1 = set()
    main_student_set2 = set()
    components_set1 = set()
    components_set2 = set()
    component_intersect_set = set()
    component_intersect_list = []

    for stuid, stuname in stu.items():
        if stuname[0] == studentName1:
            req_stuid1 = stuid
        elif stuname[0] == studentName2:
            req_stuid2 = stuid
        else:
            continue

    #print(req_stuid1+"   "+req_stuid2)
    if req_stuid1 not in stu or req_stuid2 not in stu:
        return None
    else:
        circuit_files = glob.glob("Circuits/*")
        for file in circuit_files:

            with open(file, "r") as f:
                flines = f.readlines()
                participant_line = flines[1].strip()
                participants = participant_line.split(", ")
                no_of_participants = len(participants)
                for j in range(no_of_participants):
                    if participants[j] == req_stuid1:
                        components_line1 = flines[4].strip()
                        components1 = components_line1.split(", ")
                        components_set1 = set(components1)
                        main_student_set1.update(components_set1)

                    elif participants[j] == req_stuid2:
                        components_line2 = flines[4].strip()
                        components2 = components_line2.split(", ")
                        components_set2 = set(components2)
                        main_student_set2.update(components_set2)
                        #flag2 = 1
                    else:
                        continue


                    components_intersect_set = main_student_set2.intersection(main_student_set1)
        #print(components_intersect_set)
        components_intersect_list = list(components_intersect_set)
        components_intersect_list.sort()
        #print(components_intersect_list)


        return components_intersect_list
        #return components_list

#Prob 10
def getProjectByCircuit():
    circuits = {}
    projects = {}
    projects2 = {}
    circuits = _make_circuits_dictionary()
    for projid, circuit_list in circuits.items():
        no_ckts_list = len(circuit_list)
        for i in range(no_ckts_list):
            projects = _make_dictionary_set(circuit_list[i], projid, projects)
    for cktid, proj_list in projects.items():
        proj_list = list(projects[cktid])
        proj_list.sort()
        for j in range(len(proj_list)):
            projects2 = _make_dictionary(cktid, proj_list[j], projects2)
    return projects2

#Prob 11
def getCircuitByStudent():
    import glob
    stu = {}
    work = {}
    work2 = {}
    stu = _make_student_dictionary()
    circuit_files = glob.glob("Circuits/*")
    for file in circuit_files:
        with open(file, "r") as f:
            flines = f.readlines()
        participant_line = flines[1].strip()
        participants = participant_line.split(", ")
        no_of_participants = len(participants)
        circuit_fname = file
        interim_circuit_fname1 = circuit_fname.split("_")
        interim_circuit_fname2 = interim_circuit_fname1[1].split(".")
        circuit_name = interim_circuit_fname2[0]
        for stuid, stuname in stu.items():
            for j in range(no_of_participants):
                if participants[j] == stuid:
                    work = _make_dictionary_set(stuname[0], circuit_name, work)
                else:
                    continue
    for studentname, ckts in work.items():
        ckts_list = list(work[studentname])
        ckts_list.sort()
        for k in range(len(ckts_list)):
            work2 = _make_dictionary(studentname, ckts_list[k], work2)
    #print(work2)
    return work2

#Prob12
def getCircuitByStudentPartial(studentName):
    import glob
    stu = {}
    work = {}
    work2 = {}
    flag = 0
    stu = _make_student_dictionary()
    circuit_files = glob.glob("Circuits/*")
    for file in circuit_files:
        with open(file, "r") as f:
            flines = f.readlines()
        participant_line = flines[1].strip()
        participants = participant_line.split(", ")
        no_of_participants = len(participants)
        circuit_fname = file
        interim_circuit_fname1 = circuit_fname.split("_")
        interim_circuit_fname2 = interim_circuit_fname1[1].split(".")
        circuit_name = interim_circuit_fname2[0]
        for stuid, stuname in stu.items():
            names = stuname[0].split(", ")
            first_name = names[0].strip()
            last_name = names[1].strip()
            if first_name == studentName or last_name == studentName:
                flag = 1
                for j in range(no_of_participants):
                    if participants[j] == stuid:
                        work = _make_dictionary_set(stuname[0], circuit_name, work)
                    else:
                        continue
            else:
                continue

    if flag == 0:
        return None
    else:
        for studname, ckts in work.items():
            ckts_list = list(work[studname])
            ckts_list.sort()
            for k in range(len(ckts_list)):
                work2 = _make_dictionary(studname, ckts_list[k], work2)

        return work2


#Main function
if __name__ == "__main__":
    #getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6")
    #print(getComponentCountByStudent("Scott"))
    #print(getParticipationByStudent("Adams, Keith"))
    #print(len(getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6")))
    #components = {"T71.386", "C407.660", "L760.824", "R497.406"}
    #compList2 = ['T475.274','C471.636']
    #components = set(compList2)
    #print(getProjectByComponent(components))
    #components = ['T475.274', 'C471.636']
    #print(getStudentByComponent(components))
    #studentNames = {"Young, Frank", "Reed, Bobby", "Butler, Julia", "Sanchez, Deborah"}
    #print(getComponentsByStudents(studentNames))
    #studentNames = set(['Adams, Keith'])
    #print(getComponentsByStudents(studentNames))
    #print(getCommonByProject("0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A", "D88C2930-9DA4-431F-8CDB-99A2AA2C7A05"))
    #print(getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "90BE0D09-1438-414A-A38B-8309A49C02EF"))
    print(getCommonByStudent("Edwards, Rachel", "Ward, Sandra"))
    #print(getProjectByCircuit())
    #print(getCircuitByStudent())
    #print(getCircuitByStudentPartial("Scott"))
