# Cellular Automata

This Python package implements 2-d cellular automata by using pytorch.
This package includes two types of 2-d cellular automata:

1. **Totalistic CAs**: cells update by the sum of its neighbors' (including it self) states;
2. **Outer-totalistic CAs**: cells update by the sum of its neighbors' (NOT including it self) states AND the cells' state;

for more information, see:
```
Packard, Norman H., and Stephen Wolfram. "Two-dimensional cellular automata."
Journal of Statistical physics 38.5 (1985): 901-946.
```

# Install

```bash
git clone https://github.com/Zhangyanbo/Cellular_Automata
cd Cellular_Automata/
python setup.py install
```

# Basic Usage

### Game of Life

```python
import CA
import matplotlib.pyplot as plt


s = CA.GameOfLife(init_state=CA.random_init(150), steps=150)

plt.figure(figsize=(8, 8))
plt.imshow(1-s, cmap='gray')
plt.show()
```

### Totalistic CAs

```python
import CA
import matplotlib.pyplot as plt


s = CA.TotalisticCA(30, init_state=CA.random_init(150), steps=150)

plt.figure(figsize=(8, 8))
plt.imshow(1-s, cmap='gray')
plt.show()
```

### Outer-totalistic CAs

```python
import CA
import matplotlib.pyplot as plt


s = CA.OuterTotalisticCA(20, init_state=CA.random_init(150), steps=150)

plt.figure(figsize=(8, 8))
plt.imshow(1-s, cmap='gray')
plt.show()
```