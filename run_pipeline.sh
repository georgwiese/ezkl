#! /bin/bash

set -e

echo "=== Generating SRS"
ezkl gen-srs --logrows 17 --params-path=kzg.params

echo "=== Generating keys"
ezkl setup -M network.onnx --params-path=kzg.params --vk-path=vk.key --pk-path=pk.key --circuit-params-path=circuit.params

echo "=== Generating proof"
ezkl prove -M network.onnx -D input.json --pk-path=pk.key --proof-path=model.proof --params-path=kzg.params --circuit-params-path=circuit.params

echo "=== Verifying proof"
ezkl verify --proof-path=model.proof --circuit-params-path=circuit.params --vk-path=vk.key --params-path=kzg.params
