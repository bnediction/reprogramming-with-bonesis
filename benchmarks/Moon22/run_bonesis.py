# argument: k (maximum number of perturbation)
# argument: mode (P1 by default)
# to be launched with parameter lambda in a folder containing
# - inputs.json
# - transition_formula.bnet
# files
import sys
import json
import bonesis
from bonesis.reprogramming import *
with open("inputs.json") as fp:
    inputs = json.load(fp)
f = bonesis.BooleanNetwork("transition_formula.bnet")
k = int(sys.argv[1])
M = {"p": 1}

mode = sys.argv[2] if len(sys.argv) > 2 else "P1"
limit = int(sys.argv[3]) if len(sys.argv) > 3 else None

assert mode in ["P1", "P3"]

if mode == "P1":
    generator = marker_reprogramming_fixpoints(f, M, k,
        exclude=inputs["uncontrollable_vars"])
elif mode == "P3":
    generator = marker_reprogramming(f, M, k,
        exclude=inputs["uncontrollable_vars"])

if limit is None:
    for sol in generator:
        print(sol)
else:
    for i, sol in enumerate(generator):
        print(sol)
        if i == limit - 1:
            break
