# `mypy --install-types` Usability Issue

## Summary

When no `.mypy_cache` folder exists and a user runs
`mypy --install-types --non-interactive ./`, `mypy` may fail on fundamental
Python issues but suggest that the failure was because of "no mypy cache
directory," confusing the user.

## Reproduction

**Environment**

Ubuntu 20, Python 3.6, mypy 0.910. (The old Python version reflects the setup of
a production codebase where this issue was discovered.)

**Confirm The Failure**

Using this repo as-is, first run `main.py` to confirm it works.

```
$ python3 main.py
test
```

Then, run mypy.

```
$ mypy --version
mypy 0.910
$ mypy --install-types --non-interactive ./
error: --install-types failed (no mypy cache directory)
```

We can provoke success by creating an empty cache directory and running mypy
again.

```
$ mkdir .mypy_cache
$ mypy --install-types --non-interactive ./
b/lib.py: error: Duplicate module named "lib" (also at "./a/lib.py")
b/lib.py: note: Are you missing an __init__.py? Alternatively, consider using --exclude to avoid checking one of them.
Found 1 error in 1 file (errors prevented further checking)
```

Address the errors, _remove `.mypy_cache`_, and run mypy again.

```
$ touch a/__init__.py
$ touch b/__init__.py
$ rm -r .mypy_cache/
$ mypy --install-types --non-interactive ./
main.py:2: error: Incompatible types in assignment (expression has type "str", variable has type "int")
Found 1 error in 1 file (checked 5 source files)
```
