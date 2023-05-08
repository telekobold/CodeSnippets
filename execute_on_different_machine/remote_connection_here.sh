#!/bin/sh

user="fritzhoppenstedt"
host="example.com"

# "2> /dev/null" suppresses the error message "Pseudo-terminal will not be
# allocated because stdin is not a terminal."
ssh $user@$host 2> /dev/null << EOF
    ls -ahl;
    pwd;
    whoami;
EOF

