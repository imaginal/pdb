def pdb_init():
    # return to debugger after fatal exception (Python cookbook 14.5):
    def return_to_debugger(type, value, tb):
        if hasattr(sys, 'ps1') or not sys.stderr.isatty():
            sys.__excepthook__(type, value, tb)
        import traceback, pdb
        traceback.print_exception(type, value, tb)
        print
        pdb.pm()
 
    sys.excepthook = return_to_debugger
    histfile = ".pdb_history"
    import readline
    try: readline.read_history_file(histfile)
    except IOError: pass
    import atexit
    atexit.register(readline.write_history_file, histfile)
    readline.set_history_length(200)

pdb_init()
del pdb_init
