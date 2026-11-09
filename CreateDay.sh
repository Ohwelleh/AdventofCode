#!/bin/bash

# shellcheck disable=SC1091

main() {
    . ./.env
    local local_dir
    local_dir="AdventCode/$1/day$2"


    echo "Setting up structure for day $2, $1..."

    # Day structure
    mkdir -p "$local_dir"
    curl -X GET -s --cookie "session=$ADVENT_OF_CODE_SESSION_ID" https://adventofcode.com/"$1"/day/"$2"/input >"$local_dir"/input.txt
    cp AdventCode/template.py "$local_dir"/solution.py
    touch "$local_dir"/sample.txt
    # sleep 0.1
    # sed -i "" "s;day0;day$2;g;" "$local_dir"/solution.py
    # sed -i "" "s;2000;$1;g;" "$local_dir"/solution.py

}

main "$@"