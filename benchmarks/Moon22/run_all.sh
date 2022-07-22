#!/usr/bin/env bash
TIMEOUT="10m"
set -x
for P in "P1" "P3"; do
    for k in 1 2 4 6; do
        bash make_experiment.sh ${TIMEOUT} ${k} ${P} 1  > timing_${P}_${k}_lim1.csv
        bash make_experiment.sh ${TIMEOUT} ${k} ${P} 100  > timing_${P}_${k}_lim100.csv
        bash make_experiment.sh ${TIMEOUT} ${k} ${P} > timing_${P}_${k}.csv
    done
done
