#! /usr/bin/env python3.4
import sys
import re
import glob
from exModule import runNetworkCode

#Part 1
def checkNetwork(**kwargs):
    try:
        runNetworkCode(kwargs)
        return True
    except OSError as o:
        err = type(o).__name__
        print("An issue encountered during runtime. The name of the error is : %s" %(err))
    except ConnectionError as c:
        raise
    except:
        return False

#Part 2
def isOK(signalName):
    exp = r'[A-Z]{3}\-[0-9]{3}'
    if re.match(exp, signalName):
        return True
    else:
        return False

def loadDataFrom(signalName, folderName):
    if isOK(signalName):
       signal_path = folderName+"/"+signalName+".txt"
       float_list = []
       non_float_count = 0
       try:

           with open(signal_path, 'r') as f:
               lines = f.readlines()
       except:
           raise OSError(2, 'No such file', signalName)
       else:
           for line in lines:
                num = line.strip()
                exp = r'\-?[0-9]+\.[0-9]+'
                if(re.match(exp, num)):
                    float_list.append(float(num))
                else:
                    non_float_count = non_float_count + 1

           tup = (float_list, non_float_count)
           return tup

    else:
        raise ValueError("%s is invalid." %signalName)

def isBounded(signalValues, bounds, threshold):
    min_bound = bounds[0]
    max_bound = bounds[1]
    out_of_bound_cnt = 0
    #print(min_bound)
    #print(max_bound)
    if (len(signalValues) == 0):
        raise ValueError("Signal contains no data.")
    else:
        for val in signalValues:
            if((val <= min_bound) or (val >= max_bound)):
                #print("Dw I'm here")
                out_of_bound_cnt = out_of_bound_cnt + 1
            else:
                #print("ugh")
                continue
        #print(out_of_bound_cnt)
        if(out_of_bound_cnt <= threshold):
            return True
        else:
            return False


if __name__ == "__main__":

    #checkNetwork(kwargs)
    #print(loadDataFrom("IWR-395", "Signals"))
    sig_list = [90.9, 80.6, 6.7, 5.8]
    sig_list2 = []
    bounds = (6, 90)
    thresh = 3
    print(isBounded(sig_list, bounds, thresh))
