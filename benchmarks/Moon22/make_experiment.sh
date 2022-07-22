#!/usr/bin/env bash
timeout=$1; shift
k=$1; shift
mode=$1; shift
limit=$1
set -x
for x in *_*_*; do
    echo -n $x,
    cd $x
    S=${SECONDS}
    timeout ${timeout} python ../run_bonesis.py ${k} ${mode} ${limit} >&2
    E=${SECONDS}
    T=$((${E} - ${S}))
    cd ..
    echo ${T}
done

