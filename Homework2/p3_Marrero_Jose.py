# Name: Jose Marrero
# Z number: Z23816617

import csv
def add_user(sn: dict, username: str, fullname: str) -> bool:
    """Add a new user with an empty friends list to the social network.

    Args:
        sn: Social network dictionary
        username: The new user's username
        fullname: The new user's full name

    Returns:
        True if added
        False if the username exists already
    """
    empty_friend_list = []
    try:
        if username in sn:
            return False

        sn[username] = (fullname, empty_friend_list)
        return True

    except KeyError:
        print("Unable to add the user because a required key is missing.")
    raise

# Step B

def add_friend(sn: dict, user1: str, user2: str) -> bool:
    try:
        if user1 not in sn or user2 not in sn:
            return False
            

        if user2 not in sn[user1][1]:
            sn[user1][1].append(user2)
        if user1 not in sn[user2][1]:
            sn[user2][1].append(user1)
        return True

    except KeyError:
            print("Unable to add the user because a required key is missing.")
            raise

# Step C
def get_friends(sn: dict, user1: str, distance: int) -> list:
    """takes a dictionary sn with a social network, an username in argument user1, and a positive integer in argument distance and that returns a list with all
friends of user1 at link distance 1, 2, …, distance."""
    try: 
        if user1 not in sn:
            return []

        result_list = []

        visited = [user1]
        current_group = [user1]

        for step in range(distance):
            next_group = []
            for person in current_group:
                
                for friend in sn[person][1]:
                    if friend not in visited:
                        visited.append(friend)
                        result_list.append(friend)
                        next_group.append(friend)
            current_group = next_group
        return result_list
    except KeyError:
        print("Unable to retrieve friend/s. User record is missing")
    raise

# Step D

def save_network(filename: str, sn: dict) -> None:
    """saves a social network dictionary to a .CSV file. 
    The function takes as parameter the file name and the dictionary. Let your function throw relevant exceptions, e.g. FileNotFoundError."""
    try:
        with open(filename, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            for user_name in sn:
                full_name = sn[user_name][0] 
                friends = sn[user_name][1]

                csv_row = [user_name, full_name] + friends
                csv_writer.writerow(csv_row)
    except OSError:
        print("Unable to save the network. Please check the filename and file permissions are valid")
        raise

# Step E

def load_network(filename: str) -> dict:
    """ reads a social network from a .CSV file saved with
save_network(…) and that returns the dictionary object"""
    sn = {}
    try:
        with open(filename, "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                username = row[0]
                fullname = row[1]
                friends = row[2:]
                sn[username] = (fullname, friends)
        return sn
    except OSError:
        print("Wasn't able to load the network. Please check the filename and file permissions are valid")
        raise

# Step F

def main() -> None:
    network = {}
    print(add_user(network, "jose", "Jose Marrero"))
    print(add_user(network, "jose", "Jose Marrero"))
    print(add_user(network, "tommy", "Tom Smith"))
    print(add_user(network, "carlll", "Carl Brown"))

    print(add_friend(network, "jose", "tommy"))
    print(add_friend(network, "tommy", "carlll"))
    print(network)

    print(get_friends(network, "jose", 1))
    print(get_friends(network, "jose", 2))
    print(get_friends(network, "missing_user", 1))

    save_network("problem3_network.csv", network)
    loaded_network = load_network("problem3_network.csv")
    print("Loaded network matches:", loaded_network == network)


main()