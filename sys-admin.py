"""
System administration using python
"""

import os
# os.system("ls")

import subprocess
subprocess.run(["ls"])

# using multiple args with subprocess.run
# subprocess.run(["ls","-l"])
subprocess.run(["ls","-l","README.md"])


# gather system info using the command uname
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
# subprocess.run([command,commandArgument])

# gather disk info using the command ps
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])