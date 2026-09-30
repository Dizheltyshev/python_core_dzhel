import test_data

count = int(input("Сколько тестовых пользователей создать? "))

users = []

for number in range(count):
    user = test_data.generate_user()
    users.append(user)

print("\nТестовые пользователи")
for user in users:
    print(f"{user['login']} — {user['age']} лет — {user['status']}")

active = 0
blocked = 0
inactive = 0

for user in users:
    if user["status"] == "ACTIVE":
        active += 1
    elif user["status"] == "BLOCKED":
        blocked += 1
    elif user["status"] == "INACTIVE":
        inactive += 1

print("\nСтатистика по статусам")
print(f"ACTIVE: {active}")
print(f"BLOCKED: {blocked}")
print(f"INACTIVE: {inactive}")