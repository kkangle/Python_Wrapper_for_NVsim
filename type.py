import subprocess
import os

all_file_list = ["sample_PCRAM.cfg",
                 "sample_SLCNAND.cfg",
                 "sample_STTRAM_macro.cfg",
                ]

all_type_list = ["PCRAM", "SLCNAND", "STTRAM"]

def get_parameter(filename) :
    fchange = open(filename, 'r')
    first = True
    para_list = []
    for line_in_change in fchange:
        if first:
            main_para = line_in_change
            first = False
        if line_in_change == '\n':
            pass
        elif "var_str" in line_in_change:
            line_split = line_in_change.split(':')
            var_str = (line_split[len(line_split) - 1]).strip()
    fchange.close()
    return main_para, var_str


def replace_line(filename, main_para):
    with open("temp.cfg", 'w') as new_file:
        with open(filename) as old_file:
            for line in old_file:
                if main_para[0:8] in line:
                    new_file.write(main_para)
                else:
                    new_file.write(line)
    os.remove(filename)
    os.rename("temp.cfg", filename)


def open_all_files(main_para):
    for f in all_file_list:
        replace_line(f,main_para)

def call_subprocess(var_str):
    final_list = []
    final_list_len = 0
    foutput = open("output", 'w')
    for f in all_file_list:
        print f
        try:
            foutput.write(subprocess.check_output(['./nvsim', f]))
        except:
            print("no valid solution for" + f)
        foutput.close()
        foutput = open("output", "r")
        for line in foutput:
            if var_str in line:
                line_split = line.split(':')
                final_list.append((line_split[len(line_split) - 1]).strip())
        if final_list_len == len(final_list):
           print "no solution"
        else:
           print final_list[final_list_len - 1]
    return final_list


#def get_result(var_str):
#    foutput = open("output", "r")
#    final_list = []
#    for line in foutput:
#        if var_str in line:
#            line_split = line.split(':')
#            final_list.append((line_split[len(line_split) - 1]).strip())
#    return final_list


para, var_str = get_parameter("change")
open_all_files(para)
result_list = call_subprocess(var_str)
print(result_list)


plt.scatter(all_type_list, result_list, s=area, c=colors, alpha=0.5)
plt.plot(all_type_list,result_list)
plt.title('result')
plt.xlabel(all_type_list)
plt.ylabel(result_list)
plt.show()

