#rund dir()
#find load, dump, loads, dumps
#run help()
#Understand: file vs string difference

#import json
#dir(json)
#help(json.load)
#load(
#    fp,
#    *,
#    cls=None,
#    object_hook=None,
#    parse_float=None,
#    parse_int=None,
#    parse_constant=None,
#    object_pairs_hook=None,
#    **kw
#-- More  --
#help(json.dump)
#dump(
#    obj,
#    fp,
#    *,
#    skipkeys=False,
#    ensure_ascii=True,
#    check_circular=True,
#    allow_nan=True,
#    cls=None,
#    indent=None,

#etc..

#File vs. String
#In Python, a string is an immutable sequence of 
# characters stored in volatile memory, while a file 
# is a named, persistent storage location on a non
# -volatile medium like a disk. 

import sys

# Get the string from the command line arguments
# sys.argv[0] is the script name, so sys.argv[1] is the first argument
if len(sys.argv) > 1:
    user_string = sys.argv[1]
    print(f"Received string: {user_string}")
else:
    print("No string provided as argument. Using default string.")
    user_string = "This is a default string in memory."
    print(f"Default string: {user_string}")
