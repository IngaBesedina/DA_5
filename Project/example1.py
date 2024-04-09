import pathlib
import collections


print(collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir()))
print(collections.Counter(p.suffix for p in pathlib.Path.cwd().glob('*.p*')))