
import os
import subprocess
 
code = subprocess.Popen(['/mnt/c/Xming/Xming.exe', '-multiwindow', '-clipboard'])
if code.returncode == 0:
    print('Alive')
else:
    print('Unreachable')

#":0 -clipboard -multiwindow"
#, stdout=subprocess.DEVNULL