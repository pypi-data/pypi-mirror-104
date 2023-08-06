## Poolformer

My own attempt at an efficient attention solution. The idea is pretty simple. The entire network will be composed of local attention. However, at the start, one pools a copy of the sequence into a shorter sequence.

All local attention windows can attend to its own window, the ones adjacent, and all of the pooled tokens (with proper masking in the autoregressive case to make sure the past does not attend to a future pooled token).

Optionally one can have the pooled tokens undergo its own self-attention (which will be negligible due to its length), allowing the network to process and pass higher-order information around and then back to the original set of tokens.

- [ ] experiments pending

## Install

```bash
$ pip install poolformer
```

## Usage

```python
import torch
from poolformer import Poolformer

model = Poolformer(
    num_tokens = 20000,
    dim = 512,
    depth = 4,
    max_seq_len = 1024,
    window_size = 128
)

x = torch.randint(0, 20000, (1, 1024))

model(x) # (1, 1024, 20000)
```
