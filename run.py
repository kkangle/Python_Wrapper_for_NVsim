import subprocess
import linecache
import re
import panda as pd
import matplotlib.pyplot as plt

# open change file and get parametes 
def get_parameter(filename):
    fchange = open(filename, 'r')
    linecount = 0;
    var_num = 0;
    para_list = []
    for line_in_change in fchange:
        if(line_in_change == "\n"):
            pass
        elif("var_num" in line_in_change):
            line_split = line_in_change.split(':')
            var_num = int(line_split[len(line_split) - 1])  
        elif(linecount == 0):
            para_name = line_in_change.strip()
        else:
            line_in_change = line_in_change.strip() 
            para_list.insert(linecount, line_in_change)
        linecount = linecount + 1
    fchange.close()
    return var_num, para_name, para_list

# helper for getting specific line 
def get_line(filename, n):
    with open(filename, 'r') as f:
        for line_number, line in enumerate(f):
            if line_number == n - 1:
                return line

def get_result(para_name, para_list, var_num):
    count = 0
    rst_list = []
    para_name_split = para_name.split(" ")
   
    # loop through all the parameter and call
    # main method every time, then write to a file
    for data in para_list[0:len(para_list)]:
        finter = open('inter.cfg', 'w')
        fcleanup = open('cleanup.cfg', 'r')
        foutput = open('output', 'w')
        for line_in_cleanup in fcleanup:
            if para_name_split[0] not in line_in_cleanup:
                pass
            else:
                #splitlist = line_in_cleanup.split(" ")
                #splitlist[len(splitlist) - 1] = data + "\r\n"
                finter.write(' '.join(para_name_split) + data + "\r\n")
                print ' '.join(' '.join(para_name_split) + data + "\r\n")
    
        fcleanup.close()
        finter.close()
        foutput.write(subprocess.check_output(['./nvsim', 'inter.cfg']))
        foutput.close()

        # get the specific result that we want
        line = get_line('output', var_num)
        line_split = re.split('[:\-=]+', line)
        rst_name = line_split[1].strip()
        result_value = line_split[len(line_split) - 1].strip()
        value = int(re.search(r'\d+', result_value).group())
        rst_list.insert(count, value)
        print(value)
        count+=1
    return rst_name, rst_list

# main program
var_num, para_name, para_list = get_parameter('change')
print "var_num : ", var_num
print "Data Name : ", para_name
print "Data List : ", para_list
#para_name = para_list[0]
#print para_name

rst_name, rst_list = get_result(para_name, para_list, var_num)
print "Result Name : ", rst_name
print "Result List : ", rst_list

area = 10
colors =(0,0,0)

plt.scatter(para_list, rst_list, s=area, c=colors, alpha=0.5)
plt.plot(para_list,rst_list)
plt.title('result')
plt.xlabel(para_name)
plt.ylabel(rst_name)
plt.show()




