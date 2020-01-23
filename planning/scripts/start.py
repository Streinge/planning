
import os
import subprocess
 
code = subprocess.call(['/mnt/c/Xming/Xming.exe', '-multiwindow', '-clipboard'])
time.sleep(5)
  
time.kill()
if code == 0:
    print("Success!")
else:
    print("Error!")
#":0 -clipboard -multiwindow"
