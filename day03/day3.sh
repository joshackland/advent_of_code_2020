#!/bin/bash

declare -a map
index=0
while read -r input; do
    map[index]=$input
    let index++
done < file.txt
#PART 1
tree_counter=0
right=0
right_len=${#map[0]}

counter = 0
for row in ${map[@]}; do
    if [[ $counter -gt 0 ]]; then
        let right=($right+3)%$right_len
        if [ ${row:right:1} == '#' ]; then
            let tree_counter++
        fi
    fi
    let counter++
done

echo $tree_counter

#PART 2
