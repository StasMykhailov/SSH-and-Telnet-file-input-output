scrooge
File input/output using SSH and Telnet
Running
--------------

Using Makefile
^^^^^^^^^^^^^^^^^^^^^

*  to start project run:

    $ make build_core
    $ make start_core

*  to stop project run:

    $ make stop_core

*  to run tests run:

    $ make run_tests

* to run command to read from file run:
    
    docker-compose exec core python core/commands.py {method: SSH or Telnet} {name of host} {name of port} {remote username} {remote password} read {path to remote file}

* to run command to write text to file run:
    
    docker-compose exec core python core/commands.py {method: SSH or Telnet} {name of host} {name of port} {remote username} {remote password} write {path to remote file} {text}