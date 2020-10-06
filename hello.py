import subprocess
import time

def islocked():
    time.sleep(5)
    process_name='LogonUI.exe'
    callall='TASKLIST'
    outputall=subprocess.check_output(callall)
    outputstringall=str(outputall)
    if process_name in outputstringall:
        print("Locked.")
    else: 
        print("Unlocked.")
    
islocked()