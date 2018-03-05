#! /usr/bin/env python3.4
import glob
import moduleTasks

def _make_dictionary(dictionary, key, value):
    """if key not in dictionary:
        elem_list = []
        dictionary[key] = elem_list
        dictionary[key] = value
    else:
        dictionary[key].append(value)"""
    dictionary[key] = value
    return dictionary

def loadMultiple(signalNames, folderName, maxCount):
    sig_dictionary = {}
    folder_path = folderName+"/*"
    sig_files = glob.glob(folder_path)
    for sig in signalNames:
        #if(sig not in sig_files):  //Why would this method not work???
            #sig_dictionary = _make_dictionary(sig_dictionary, sig, None)
        if(not(moduleTasks.isOK(sig))):
            sig_dictionary = _make_dictionary(sig_dictionary, sig, None)
        else:
            try:
                test_tup = moduleTasks.loadDataFrom(sig,folderName)
            except:
                sig_dictionary = _make_dictionary(sig_dictionary, sig, None)
            else:
                sig_val_list = test_tup[0]
                sig_non_float_cnt = test_tup[1]
                if(sig_non_float_cnt <= maxCount):
                    sig_dictionary = _make_dictionary(sig_dictionary, sig, sig_val_list)
                else:
                    emp_list = []
                    sig_dictionary = _make_dictionary(sig_dictionary, sig, emp_list)
    return sig_dictionary

def saveData(signalsDictionary, targetFolder, bounds, threshold):
    #emp_list = []
    for sig, sig_val in signalsDictionary.items():
        #if (sig_val == None):
            #continue
        #elif(len(sig_val) == 0):
        #    continue
        #else:
            try:
                #print(moduleTasks.isBounded(sig_val, bounds, threshold))
                if(moduleTasks.isBounded(sig_val, bounds, threshold)):
                    path = targetFolder+"/"+sig+".txt"

                    #print(path)

                    #print("Now this is just stupid -.-")

                    with open(path, 'w') as f:
                        for val in sig_val:
                            f.write('%.3f \n' %val)

                else:
                    continue
            except:
                pass



if __name__ == "__main__":
    sig_names = ["FPT-701", "ABC", "VKY-370", "IWR-390", "IWR-395", "REY-386"]
    sig_dict = {}
    sig_dict = loadMultiple(sig_names, "Signals", 9)
    #print(sig_dict)
    bounds = (-5, 1000)
    thresh = 100
    saveData(sig_dict, "targf", bounds, thresh)
