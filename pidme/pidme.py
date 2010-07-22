import os
import atexit

def register_pidfile(pidfile):
    if os.path.isfile(pid):
        return False
    
    file(pidfile, 'w').write(str(os.getpid()))
    atexit.register(clear_pid, pidfile=pidfile)
    return True
    
def clear_pidfile(pidfile):
    os.remove(path)