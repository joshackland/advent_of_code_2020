#!/bin/bash

#PART 1
valid_passwords=0

while read -r input; do
    line=($(echo $input | tr " " "\n"))
    nums=($(echo ${line[0]} | tr "-" "\n"))
    num1=${nums[0]}
    num2=${nums[1]}
    letter=($(echo "${line[1]/:/}"))
    password=${line[2]}
    
    counter=0
    
    for l in $(seq 1 ${#password}); do
        if [ ${password:l-1:1} == $letter ]; then
            let counter++
        fi
    done

    if [ "$counter" -ge "$num1" ] && [ "$counter" -le "$num2" ]; then        
        let valid_passwords++
    fi
done < file.txt

echo "Valid Passwords: ${valid_passwords}"

#PART 2
valid_passwords=0

while read -r input; do
    line=($(echo $input | tr " " "\n"))
    nums=($(echo ${line[0]} | tr "-" "\n"))
    num1=${nums[0]}
    num2=${nums[1]}
    letter=($(echo "${line[1]/:/}"))
    password=${line[2]}
    
    if [ "${password:${num1}-1:1}" = "$letter" ] || [ "${password:${num2}-1:1}" = "$letter" ]; then
        let valid_passwords++
        if [ "${password:${num1}-1:1}" = "$letter" ] && [ "${password:${num2}-1:1}" = "$letter" ]; then
            let valid_passwords--
        fi
    fi
done < file.txt

echo "Valid Passwords: ${valid_passwords}"