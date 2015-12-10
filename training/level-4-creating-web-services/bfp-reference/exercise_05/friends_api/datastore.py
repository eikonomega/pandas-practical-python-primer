_friends = [
    {
        "id": "BFP",
        "firstName": "Big Fat",
        "lastName": "Panda",
        "telephone": "574-213-0726",
        "email": "mike@eikonomega.com",
        "notes": "My bestest friend in all the world."
    },
    {
        "id": "VinDi",
        "firstName": "Vin",
        "lastName": "Diesel",
        "telephone": "I-HIT-PEOPLE",
        "email": "vdiesel4@supercool.edu",
        "notes": "Really annoying guy.  Will never amount to anything."
    }
]


def friends() -> list:
    """
    Provide a list of friends.

    Returns:
        A `list` containing dictionaries for each friend.
    """
    return _friends


def friend(id: str) -> dict:
    """
    Provide data on a single friend.

    Args:
        id: A str of the unique identifier to look for in our list of friends.

    Returns:
        A dict of data on the designated fried or None if not match is found.
    """
    for possible_match in _friends:
        if id.lower() == possible_match['id'].lower():
            return possible_match