Pidme - Pidfile creation and cleanup
====================================

	import pidme
	
	if pidme.register_pidfile("/tmp/mypidfile.pid"):
		//do lots of stuff
		
Pidme uses the atexit module to register a function to automatically clear your pidfile.  If you must do it yourself pass your pidfile in to clear_pidfile.

	pidme.clear_pidfile("/tmp/mypidfile.pid")
	
Known Problems
--------------
Because we are not locking the pidfile, there is a small chance that pidme could see there is no file and open and write to the pidfile at the same time as another script.  Don't do that.  This script was written to keep long running jobs from overwriting each other.