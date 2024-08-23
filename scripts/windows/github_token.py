import win32cred
import sys

target_name = "git:https://github.com"

try:
    creds = win32cred.CredRead(
        Type=win32cred.CRED_TYPE_GENERIC, TargetName=target_name)
    if creds:
        username = creds['UserName']
        password = creds['CredentialBlob'].decode('utf-16')
        print(f"Username: {username}")
        print(f"Password: {password}")
    else:
        print("No credentials found for target", target_name)
except Exception as e:
    print("Failed to read credentials:", str(e))
    sys.exit(1)
