# lifeproof
Create proofs of life to detect when a program fails.

## Create a file proof of life

To create a file proof of life is very simple. You only need to execute:

```python
from lifeproof import FileProofOfLife

with FileProofOfLife('file_path'):
       something_to_do()
```

Where 'file_path' is the file path to the proof of life to check. If this file is removed, then the program has died for
any cause. The something_to_do() represent the commands to check if they are still alive. If something_to_do() breaks
down for some reason, the file automatically will be removed.

For example:

```python
from lifeproof import FileProofOfLife
from time import sleep

with FileProofOfLife('health.txt'):
       sleep(60)
```

This script will create the file 'health.txt' during 60 seconds. At the end of sleep(60) the 'health.txt' file will be
removed.
