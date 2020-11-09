
from Naked.toolshed.shell import execute_js, muterun_js
from Naked.toolshed.types import NakedObject

success = muterun_js('index.js')
print(dir(success))
print(type(success))



if success:
    print(success)
else:
    print("i hate node w/ python")

