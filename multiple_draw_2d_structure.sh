#!/bin/bash
#
# Parameters:
# 1 - File containing execution data
# 2 - Folder where the images will be save
# 3 - Digits for the output formatted number


IFS=$'\12'

format_number="%0"$3"d"
number=1
for line in $(cat ${1}); do 

#	line=$(cat ${1}|tail -1)
#	echo $line
	if [ ${line:0:11} == "Iteration: " ]; then
		number_str=$( printf $format_number $number )
		python multiple_draw_2d_structure.py $2 $number_str "${line}" 
		number=$((number+1))
	fi
	
done


