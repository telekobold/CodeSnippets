#!/bin/sh

user="fritzhoppenstedt"
host="example.com"

ssh $user@$host ls -ahl; pwd; whoami
