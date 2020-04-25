import subprocess




def local_cmd(cmd):
    return subprocess.getoutput(cmd)

def adb_cmd(cmd):
    return local_cmd('adb'+cmd)

def adb_shell_cmd(cmd):
    return adb_cmd('shell'+cmd)


l =  local_cmd('adb usb')
print(l)