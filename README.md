# Funky

Funky is a small package of a few useful functional constructs in python.

It orignated by extracting the functionnal utility functions from Gittle.

Funky has no external dependencies besides the Python standard library and Python 2.6+.

## Install

    pip install funky

## Examples


### Unique
```python
import funky

somelist = [9, 4, 9, 4, 3]

# Unique does not preserve order (could change)
# However unique preserves type, if your input is a list your output will be a list, ...
funky.unique(somelist)  # [9, 4, 3]
```


### True only
```python
import funky

# Filter out not true values
funky.true_only(["good", 9, None, True, False])  # ["good", 9, True]
```


### Pluck
```python
import funky

# Some "collection"
objects = [
    {
        'age': 55
        'other_attribute': 88
    },
    {
        'age': 33
    }
]

# Pluck works with dictionary keys as well as object attributes
# pluck preserves order
funky.pluck(objects, 'age')  # [55, 33]
```

### Hash
```python
import funky

# Hash supports hashing
funky.hash({
    'key': 'value'
})  # -8073414452536086510
```

