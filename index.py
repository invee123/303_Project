
from Naked.toolshed.shell import execute_js, muterun_js

success = execute_js('index.js')

if success:
    print(success)
else:
    print("i hate node w/ python")

