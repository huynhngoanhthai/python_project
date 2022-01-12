from werkzeug.security import generate_password_hash, check_password_hash
# Example generation
password = "123123"
print(len(generate_password_hash(password)))
diem = 0

a = ['a', 'b', 'a', 'd', 'e', 'f']
b = ['a', 'b', 'c',  'd', 'e', '2']
for i in range(1, 10):
    if a[i] == b[i]:
        diem += 1
