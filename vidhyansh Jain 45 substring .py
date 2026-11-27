secret=input("enter secret message:")
message=input("enter coded message:")
if secret in message:
    print("Secret message found:")
else:
    print("Secret message not found:")