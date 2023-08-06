# Infinite Sets

This package gives a pythonic way to deal with the universal set and set complements. Here, the universal set represents
a set that contains *everything*, whilst the *complement* of a set A is the set of everything that is not in A. This
allows the expression of concepts such as *everything* or *all but these things* in a consistent way.

The universal set may be obtained using the `everything()` function. Everything is in the universal set:

```python
from infinite_sets import everything

4 in everything()  # true
"abc" in everything()  # true
```

The complement of a set is can be created using the `complement()` function:

```python
from infinite_sets import complement

A = {1, 4}
B = complement(A)

1 in A  # true
1 in B  # false
7 in A  # false
7 in B  # true
```

Both the universal set and the set complement of a set A are *infinite sets*. Whilst you can query if a given object is
in them, you can't iterate through them in the same way you could a python set (which represents a *finite set*).

These infinite sets support all the set operations that are supported by python sets, namely equality (==), subset (<=),
strict subset (<), superset (>=), strict superset (>), intersection (&), union (|), set difference (-) and symmetric
difference (^).

They however do not support in place modification, such as (&=). This is because this could change the type of the
object.

## Example

An example of a use for infinite sets is a function that takes a set of objects, where only certain values would be
valid:

```python
from typing import Set

VALID_NAMES = {
    "chapman",
    "cleese",
    "gilliam",
    "idle",
    "jones",
    "palin"
}


def my_function(names: Set[str]):
    names = names & VALID_NAMES  # filter out invalid names
    for name in names:
        ...
```

To call this function on all the valid names, you need to have access to the set of names ahead of time and import it
from wherever it is:

```python
my_function(VALID_NAMES)
```

However, using infinite sets we could change our method to use infinite sets. By intersecting an infinite set with our
list of predefined possible names, we get the set of names the user intended to give.

The user can indicate they mean all valid names:

```python
my_function(everything())
```

Or that they want all names except `'cleese'`:

```python
my_function(complement({'cleese'}))
```

## Typing

For typing, there is an `InfiniteSet[TItem]` protocol, which defines an infinite set similarly to
the `AbstractSet[TItem]` from `collections.abc`, but without the `__iter__` or `__len__` methods. Therefore, the
universal set, set complements and all python sets are examples of an `InfiniteSet`.

If you have a method which takes an argument annotated with `Set[TItem]`, but you only check for membership of the set
and never iterate through it, you can change this annotation to `InfiniteSet[TItem]` to indicate that you could pass an
infinite set such as `everything()` to your method.

## Implementation Details

The universal set is a singleton - the `everything()` command returns the same object every time. Its `__contains__`
function returns true unconditionally.

The set complement is an object that internally stores the set of which it is a complement. Its `__contains__` function
returns true if the given item is not in its internal set.

