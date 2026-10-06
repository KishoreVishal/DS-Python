n = int(input("Enter the total number of users: "))

users = []
for i in range(n):
    name = input(f"Enter name of user {i + 1}: ")
    users.append(name)

adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

adj_list = {user: [] for user in users}

connections = int(input("\nEnter the total number of connections: "))

for i in range(connections):
    print(f"\nConnection {i + 1}:")
    user1 = input("Enter first user: ")
    user2 = input("Enter second user: ")

    if user1 not in users or user2 not in users:
        print("Invalid user name! Please enter valid users.")
        continue

    if user1 == user2:
        print("A user cannot be connected to themselves.")
        continue

    index1 = users.index(user1)
    index2 = users.index(user2)

    adj_matrix[index1][index2] = 1
    adj_matrix[index2][index1] = 1

    adj_list[user1].append(user2)
    adj_list[user2].append(user1)

print("\n========== ADJACENCY MATRIX ==========")

print("     ", end="")
for user in users:
    print(f"{user:>10}", end="")
print()

for i in range(n):
    print(f"{users[i]:>5}", end="")

    for j in range(n):
        print(f"{adj_matrix[i][j]:>10}", end="")

    print()

print("\n========== ADJACENCY LIST ==========")

for user in users:
    print(f"{user} -> {', '.join(adj_list[user])}")

print("\n========== CHECK CONNECTION ==========")

user1 = input("Enter first user to check: ")
user2 = input("Enter second user to check: ")

if user1 not in users or user2 not in users:
    print("Invalid user name!")

else:
    index1 = users.index(user1)
    index2 = users.index(user2)

    matrix_result = adj_matrix[index1][index2] == 1

    list_result = user2 in adj_list[user1]

    print("\nResult using Adjacency Matrix:")
    if matrix_result:
        print(f"{user1} and {user2} are directly connected.")
    else:
        print(f"{user1} and {user2} are not directly connected.")

    print("\nResult using Adjacency List:")
    if list_result:
        print(f"{user1} and {user2} are directly connected.")
    else:
        print(f"{user1} and {user2} are not directly connected.")
