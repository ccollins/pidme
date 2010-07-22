Pidme - Pidfile creation and cleanup
====================================

	import pidme
	
	if pidme.register_pidfile("/tmp/mypidfile.pid"):
		//do lots of stuff
		
Pidme uses the atexit module to register a function to automatically clear your pidfile.  If you must do it yourself pass your pidfile in to clear_pidfile.

	pidme.clear_pidfile("/tmp/mypidfile.pid")