#! /bin/bash

#---------------------------------------
# $Author: ee364c25 $
# $Date: 2018-01-16 17:20:32 -0500 (Tue, 16 Jan 2018) $
#---------------------------------------

# Do not modify above this line.
I=$1
rem=0
sq=0
check_ten=0
rem_ten=0
div=1
for (( k=1; k <= $1; k++ ))
do
	power=0
	power2=0
	let sq=$k*$k
	check_ten=$sq
	num3=$sq
	while (( $num3 != 0 ))
	do
		let power2=$power2+1
		let num3=$num3/10
	done
	if (( $sq/$[10**$power2] == 1 ))
	then
		echo "$sq is a power of 10"
	fi
	num=$sq
	#echo "num is $num"
	num2=$sq
	while (( $num != 0 ))
	do
		let power=$power+1
		
		let rem=$sq%$[10**$power]

		let num2=$sq/$[10**$power]
		
		
			if (( $k == $rem+$num2 ))
			then
				echo "$k is a Kaprekar number"
			fi
			let num=$num/10
		
	done
	
done
