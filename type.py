import subprocess
import re

def get_parameter(filename) :
    fchange = open(filename, 'r')
    linecount = 0
    var_str = ""
    para_list = []
    for line_in_change in fchange:
        if(line_in_change == '\n') :
            pass
        elif("var_str" in line_in_change) :
            line_split = line_in_change.split(':')
            print line_split
            var_str = ((line_split(len(line_split) - 1)).strip()
get_parameter("change")
