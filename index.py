from Naked.toolshed.shell import execute_js, muterun_js
from Naked.toolshed.types import NakedObject

success = muterun_js('index.js')
#print(dir(success))
#print(type(success))


if success:
    print('Index.js successfully run')
    #Grants solution

    #create arrays
    trump_time = []
    trump_value = []

    #read in file
    trump_f = open("trend_trump.txt", "r")
    trump = trump_f.read()
    trump_f.close()

    tax_f = open("trend_tax.txt", "r")
    tax = tax_f.read()
    tax_f.close()

    #parse necessary data
    #store parsed data in multiple arrays
        #keep indicies the same
    
    #load into ML model

else:
    print("i hate node w/ python")

