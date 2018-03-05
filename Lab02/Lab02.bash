#! /bin/bash

#----------------------------------
# $Author: ee364c25 $
# $Date: 2018-01-23 16:39:14 -0500 (Tue, 23 Jan 2018) $
#----------------------------------

function part_1 
{               
    # Fill out your answer here
	filename="people.csv"
	echo "The 9 sorted people:"
	sort -t',' -k4 -k5 -k1 -k2 -n $filename | tail -n9 
    return                      
}                               

function part_2
{              
    # Fill out your answer here
	#declare -A arr
	Arr=(a.txt b.txt c.txt d.txt e.txt)
	num=0
	num_4=0
	num_lines=0
	let num=$RANDOM%10
	#echo "$num"
	let num_4=$num%4
	echo "$num_4"
	#for ((I=0; I < 5; I++))
	#do

	#done
	filename=${Arr[$num_4]}
	echo "$filename"
	num_lines=$(wc -l $filename | cut -d' ' -f1)
	if (( $num_lines%2 == 0 ))
	then
		line1=$(head -n$(($num_lines/2)) $filename | tail -n1)
		line2=$(head -n$((($num_lines/2)+1)) $filename | tail -n1)
		echo "$line1"
		echo "$line2"
	else
		line=$(head -n$((($num_lines/2)+1)) $filename | tail -n1)
		echo "$line"
	fi
    return                     
}                              

function part_3
{
    # Fill out your answer here
	for File in src/*.c
	do
		FileName=$(echo ${File} | cut -d. -f1)
		#echo ${FileName}
		if gcc -Wall -Werror ${FileName}.c -o ${FileName}.o 2>/dev/null
		then
			echo "${FileName} : success"
		else
			#gcc -Wall -Werror ${FileName}.c -o ${FileName}.o >&2
			
			echo "${FileName} : failure"
		fi
	done
    return
}

# To test your function, you can call it below like this:
#
 part_1
 part_2
 part_3
