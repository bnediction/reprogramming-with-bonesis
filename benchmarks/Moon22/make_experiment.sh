#!/usr/bin/env bash
timeout=$1; shift
k=$1; shift
mode=$1; shift
limit=$1
set -x
for x in *_*_*; do
    if [ ! -d "$x" ]; then continue; fi
    echo -n $x,
    cd $x
    S=${SECONDS}
    timeout ${timeout} python ../run_bonesis.py ${k} ${mode} ${limit} >&2
    if [ $? -ne 0 ]; then
        T=-1
    else
        E=${SECONDS}
        T=$((${E} - ${S}))
    fi
    cd ..
    echo ${T}
done

