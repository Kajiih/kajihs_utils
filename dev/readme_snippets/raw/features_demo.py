from kajihs_utils.core import batch, get_first

# Get first key existing in a dict:
d = {"a": 1, "b": 2, "c": 3}
print(get_first(d, ["x", "a", "b"]))


# Batch a sequence:
seq = list(range(10))
list(batch(seq, 3))