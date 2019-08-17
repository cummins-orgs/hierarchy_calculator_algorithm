###########
# IMPORTS #
###########

import pandas as pd
from os.path import relpath
import numpy as np

#######################################################
# READ IN RAW DATA, INCLUDE GLOBAL VARS #
#######################################################

hr_report_df = pd.read_csv(relpath('../your_csv_file.csv'))

# Extract the relevant data from the report and get it into dictionaries for processing

name_list = list(hr_report_df['Name'].values)              # Assumes the names are clean i.e. exactly the same format as the 'reports to' column of your dataset
zero_list = zero_list = list(np.full(shape=len(hr_report_df['Name']),fill_value=0,dtype=np.int)) # Everyone starts at 0 seniority
reports_to_list = list(hr_report_df['Reports To'].values)        # Note: don't strictly need to cast these as lists, but it keeps everything consistent
seniority_dict = dict(zip(name_list,zero_list))             # Create a dictionary that stores everyone's level of seniority
supervisor_dict = dict(zip(name_list,reports_to))           # Construct supervisor dict for each supervisee. Keys are supervisees, values are supervisors

#############################
# SENIORITY LEVEL FUNCTION #
#############################

#Note: of course you can do this without introducing the dictionaries as an intermediate step;
# I just found it annoying to edit a pandas df in place or make one on the fly - ymmv! 

def seniority_level(target_name,level, supervisor_dict,seniority_dict):
    '''Recursive function to set the number of levels of hierarchy a given person is in a hierarchy
    Base case is that you are at the CEO (no supervisor) - recursive case is that you are at someone with a supervisor, so call 
    the function on them before returning. If the hierarchy level recorded for that person in seniority_dict is lower than or equal to the 
    level in the function call, update seniority_dict for that person, their level is that of the level in the function call '''
    #base case - no supervisor causes a key error because there is no supervisor
    try:
		supervisor = supervisor_dict[target_name]
    except KeyError:
        return
    if seniority_dict[target_name] <= level:
        seniority_dict[target_name] = level
    # recursive case: call at level += 1 for the supervisor
    level += 1
    new_target = supervisor
    seniority_level(new_target, level,supervisor_dict,seniority_dict)
    return

#############################################################################################
# CALL RECURSIVE SENIORITY_LEVEL FUNCTION ON ALL EMPLOYEES #
#############################################################################################

for name in seniority_dict.keys():
    seniority_level(name,0,supervisor_dict,seniority_dict) # We don't have to call the function on everyone of course, but thanks to the function setting the level, this works just fine.

# Note: after this is done, you then need to merge your seniority data back onto your hr report (name as the merge key). You can't just cast it as a series in your df, because the seniority dictionary is unordered.
