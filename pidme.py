import os
import atexit

def register_pidfile(pidfile):
    if os.path.isfile(pidfile):
        return False
    
    file(pidfile, 'w').write(str(os.getpid()))
    atexit.register(clear_pidfile, pidfile=pidfile)
    return True
    
def clear_pidfile(pidfile):
    os.remove(pidfile)