import json
from pathlib import Path
from utils import validate_password, hash_password




user = {
    "first_name": "Tolani",
    "last_name": "Akinsola",
    "email": "tolani@yahoo.com",
    "phone": "08101791765",
    "username": "black_tolani",
    "password": "password",
    "role": "OWNER"
}

def get_file_path():
    path = Path("../data/users/users.json").resolve()
    print(path)
    if path.exists():
        return path
    path.parent.mkdir(exist_ok=True, parents=True)
    path.touch(exist_ok=True)
    return path

def get_users():
    file_path = get_file_path()

    with file_path.open(mode='r', encoding='utf-8')as file:
        try:
            users = json.load(file)
            return users
        except json.decoder.JSONDecodeError:
            return []
    # try:
    #     file = file_path.open(mode='r', encoding='utf-8')
    # except (IOError, FileNotFoundError):
    #     print("File not found")
    # finally:
    #     file.close()

def save_user(user):
    user['password'] = hash_password(user['password'])

    file_path = get_file_path()
    users = get_users()

    if[u for u in users if u['username']] == user['username']:
        print(f"user with username {user['username']}already exists")
        return
    users.append(user)

    with file_path.open(mode='w', encoding='utf-8') as file:
        json.dump(users, file)

def get_user_by_username(username):
    users = get_users()
    user_list = [u for u in users if u['username'] == username]
    if user_list:
        return user_list[0]
    return f"user with username {username} not found"



if __name__ == '__main__':
    # get_file_path()
    save_user(user)
    print(get_user_by_username("black_tolani"))