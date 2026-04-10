# CNN Architecture Plot

This workspace contains a simple Python script to generate a convolutional neural network architecture diagram using Graphviz.

## Files

- `arch_plot.py`: Creates a directed graph of a CNN architecture and renders it as `cnn_structure.png`.

## Requirements

- Python 3
- `graphviz` Python package
- Graphviz system installation (for rendering)

## Install

```bash
pip install -r requirements.txt
```

On macOS, install Graphviz with Homebrew if needed:

```bash
brew install graphviz
```

## Run

```bash
python arch_plot.py
```

The script generates `cnn_structure.png` and opens it for viewing.
