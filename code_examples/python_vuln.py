import os, pickle
# Command injection
user_input = "rm -rf /"
os.system("ping " + user_input)

# Insecure deserialization
pickle.loads(user_input)
