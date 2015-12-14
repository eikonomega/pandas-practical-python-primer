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


def create_friend(data: dict):
    """
    Create a new friend entry in our datastore of friends.

    Args:
        data: A dictionary of data for our new friend.

    Raises:
        ValueError: If `data` is None.
    """
    if data is None:
        raise ValueError(
            "`None` was received when a dict was expected during "
            "the attempt to create a new friend resource.")

    required_elements = set(_friends[0].keys())
    if not required_elements.issubset(data):
        raise ValueError(
            "Some of the data elements required to create a friend "
            "were not present.  The following elements "
            "must be present to create a friend: {}".format(
                required_elements))

    # BONUS BUG
    # Use dict.keys() method to get a set of the keys.
    # Then remove non-standard data points if present.
    for element in data.copy():
        if element not in required_elements:
            data.pop(element)

    if friend(data['id']):
        raise ValueError("A friend already exists with the "
                         "`id` specified: {}".format(data['id']))

    _friends.append(data)