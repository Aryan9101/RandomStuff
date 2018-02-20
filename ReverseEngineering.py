key = "00001110"
flag = "ko}wmzhugQocQoQhbois"
password = ""
for i in range(len(flag)):
    for j in range(256):
        if chr(j^14) == flag[i]:
            password += chr(j)

print(password)
