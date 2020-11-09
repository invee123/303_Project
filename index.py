from Naked.toolshed.shell import execute_js, muterun_js
from Naked.toolshed.types import NakedObject

success = muterun_js('index.js')
#print(dir(success))
#print(type(success))

trump_f = open("trend_trump.txt", "r")
trump = trump_f.read()



if success:
    print("success")
    #Grants solution

    #create arrays
    trump_time = []

    #read in file
    trump_f = open("trend_trump.txt", "r")
    trump = trump_f.read()
    #print(type(trump))

    #parse necessary data
    #store parsed data in multiple arrays
        #keep indicies the same
    
    #load into ML model
    
else:
    print("i hate node w/ python")

