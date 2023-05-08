#!/bin/sh

user="fritzhoppenstedt"
host="example.com"

ssh $user@$host 'bash -s' < remote_commands.sh

