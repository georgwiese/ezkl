# EZKL Benchmarking

## Setup

Install the `ezkl` binary globally:

```
cargo install --path .
```


## Export ONNX models

Install Python requirements:

```
python3 -m venv env
source env/bin/activate
pip install -r requirements_test.txt
```

For example, in `examples/onnx/4l_relu_conv_fc`, run:

```
python gen.py
```

## Run proof pipeline

With `network.onnx` and `input.onnx` in your current working directory (e.g. `examples/onnx/4l_relu_conv_fc`), run:

```
<project root>/run_pipeline.sh
```