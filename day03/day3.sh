#!/bin/bash

declare -a map
index=0
while read -r input; do
    map[index]=$input
    let index++
done < <(tail +2 file.txt)
#done < file.txt

#PART 1
tree_counter=0
right=0
right_len=${#map[0]}

for row in ${map[@]}; do
    let right=($right+3)%$right_len
    if [ ${row:right:1} == '#' ]; then
        let tree_counter++
    fi
    let counter++
done

echo $tree_counter

#PART 2
part_two () {
    dir_right=$1
    dir_down=$2

    tree_counter=0
    right=$dir_right
    let down=$((dir_down - 1))

    while [ $down -lt ${#map[@]} ]; do
        if [ ${map[$down]:$right:1} == '#' ]; then
            let tree_counter++
        fi

        let right=$(((right+dir_right)%right_len))
        let down=$((down+dir_down))
    done
}

declare -a tree_list
part_two 1 1
tree_list[0]=$tree_counter

part_two 3 1
tree_list[1]=$tree_counter

part_two 5 1
tree_list[2]=$tree_counter

part_two 7 1
tree_list[3]=$tree_counter

part_two 1 2
tree_list[4]=$tree_counter

tree_product=0

for tree in ${tree_list[@]}; do
    if [[ $tree_product == 0 ]]; then
        tree_product=$tree
    else
        let tree_product="tree_product*tree"
    fi
done

echo $tree_product