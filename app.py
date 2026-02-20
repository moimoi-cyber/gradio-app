
# security/insecure_cli_only.py
# !!! TEST ONLY: SAST 検証用の故意の脆弱コード。merge禁止 !!!
import sys, subprocess

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    subprocess.run(f"echo {user_input}", shell=True)  # CWE-78: OS Command Injection
