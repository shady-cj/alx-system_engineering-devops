# Using puppet to execute a command that kills a process "killmenow"

exec { '/bin/pkill killmenow': }
