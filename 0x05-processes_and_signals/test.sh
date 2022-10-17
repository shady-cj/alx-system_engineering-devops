#!/bin/bash


if [ -z "$1" ]	
then
	top &
	echo $!
else
	echo $!
fi
