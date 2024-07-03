#!/bin/bash

SRC_DIR="/usr/local/cuda/targets/x86_64-linux/lib"
DEST_DIR="/opt/conda/lib/python3.10/site-packages/llama_cpp/lib"

for file in $SRC_DIR/*; do
    ln -s "$file" "$DEST_DIR/$(basename "$file")"
done
