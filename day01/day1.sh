#!/bin/bash

declare -a array_of_nums
declare -a sorted_array

index=0
while read l; do
    array_of_nums[$index]=$l
    let index++
done < file.txt

sorted_array=($(printf '%s\n' "${array_of_nums[@]}"|sort -n))

#Part 1
found_2020=false

i=0
j=0

while [ $i -le $(( ${#sorted_array[@]} - 2 )) ]; do
    num1=${sorted_array[$i]}
    j=$(($i + 1))
    while [ $j -le $(( ${#sorted_array[@]} -1 )) ]; do
        num2=${sorted_array[$j]}
        let sum=$((num1+num2))
        if [[ $sum -gt 2020 ]]; then
           break
        fi
        if [[ ${sum} == 2020 ]]; then
            product=$((num1*$num2))
            echo "num1 = ${num1}, num2 = ${num2}, sum = ${sum}, product = ${product}"
            found_2020=true
            break
        fi
        let j++        
    done
    let i++
done

#PART 2
found_2020=false

i=0
j=0
k=0

while [ $i -le $(( ${#sorted_array[@]} - 3 )) ]; do
    num1=${sorted_array[$i]}
    j=$(($i + 1))
    while [ $j -le $(( ${#sorted_array[@]} - 2 )) ]; do
        num2=${sorted_array[$j]}
        k=$(($j + 1))
        while [ $j -le $(( ${#sorted_array[@]} - 1 )) ]; do
            num3=${sorted_array[$k]}    
            let sum=$((num1+num2+num3))
            if [[ $sum -gt 2020 ]]; then
                break
            fi
            if [[ ${sum} == 2020 ]]; then
                product=$((num1*num2*num3))
                echo "num1 = ${num1}, num2 = ${num2}, num3 = ${num3} sum = ${sum}, product = ${product}"
                found_2020=true
                break
            fi
            let k++
        done
        let j++        
    done
    let i++
done