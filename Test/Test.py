from werkzeug.security import generate_password_hash, check_password_hash
# Example generation
password = "123123"
print(len(generate_password_hash(password)))
