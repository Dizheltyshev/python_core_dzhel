import random

def generate_login():
    names = ["test1", "test2", "test3", "test4", "test5"]
    return random.choice(names)

def generate_age():
    return random.randint(1, 99)

def generate_status():
    statuses = ["ACTIVE", "BLOCKED", "INACTIVE"]
    return random.choice(statuses)

def generate_user():
    user = {
        "login": generate_login(),
        "age": generate_age(),
        "status": generate_status()
    }
    return user