import subprocess
import hashlib
import pickle

# B101: Assert used
assert True

# B102: exec used
exec("print('Insecure')")

# B303: subprocess with shell=True
subprocess.call("ls -l", shell=True)

# B403: pickle usage
pickle.loads(b"cos\nsystem\n(S'ls'\ntR.")

# B324: weak hash
hashlib.md5(b"password").hexdigest()
