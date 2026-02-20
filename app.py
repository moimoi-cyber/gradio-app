
# security/insecure_cli_only.py
# !!! TEST ONLY: SAST 検証用の故意の脆弱コード !!!
import sys, subprocess, sqlite3, pickle, base64, hashlib

# CWE-78: OS Command Injection
if len(sys.argv) > 1:
    user_input = sys.argv[1]
    subprocess.run(f"echo {user_input}", shell=True)

# CWE-89: SQL Injection
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users(id INTEGER, name TEXT)")
cur.execute("INSERT INTO users VALUES (1, 'alice')")
cur.execute(f"SELECT * FROM users WHERE id = {user_input}")   # 脆弱
print(cur.fetchall())

# CWE-22: Path Traversal
filename = "../etc/passwd"
open(filename, "r", encoding="utf-8").read()

# CWE-502: Insecure Deserialization
data = base64.b64decode(b"gASVSwAAAAAAAACMBXBvc2l0lIwFcmFuZ2WUk5QpLg==")
obj = pickle.loads(data)

# CWE-327: Weak Crypto
hashlib.md5(b"dummy_password").hexdigest()

# CWE-798: Hardcoded Credentials (dummy secrets)
AWS_KEY = "AKIA1234567890DUMMY"
API_KEY = "api_key_dummy_123456"
PASSWORD = "P@ssw0rd!"
print(AWS_KEY[:4], API_KEY[:5], PASSWORD[:2])
