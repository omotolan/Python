import bcrypt

def hash_password(password: str):
    password = password.encode()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)


def validate_password(user_password, hashed_password):
    password = user_password.encode()
    return bcrypt.checkpw(user_password, hashed_password)


if __name__ == '__main__':
    print(hash_password("pass1235"))
    validate_password("pass1235", ha)