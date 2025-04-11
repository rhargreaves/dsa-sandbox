#!/bin/bash
set -euo pipefail

ERROR_OUTPUT_PATH=stderr.txt
export OUTPUT_PATH=stdout.txt

rm $ERROR_OUTPUT_PATH $OUTPUT_PATH || true

python3 main.py < input.txt 2>$ERROR_OUTPUT_PATH
colordiff -y <(xxd expected_output.txt) <(xxd ${OUTPUT_PATH})
