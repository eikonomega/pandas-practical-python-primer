"""
<<<<<<< HEAD
This modules provides the Datastore class which can be used for creating,
retrieving, updating, and deleting friend records from our database.
=======
This modules provides functions for creating, updating, and deleting
friend records from our database.
>>>>>>> proposed-changes
"""

import sqlite3

<<<<<<< HEAD
class Datastore:
    """
    Provides an interface to an SQLite database.
    """
    def __init__(self):
        self.connection = sqlite3.connect('/tmp/friends.db')


    def friends(self) -> list:
        """
        Return the current list of friends.

        Returns:
            Fill this in.
        """
        cursor = self.connection.execute(
            'SELECT id, firstName, lastName, telephone, email, notes '
            'FROM friends')

        friends = []
        for row in cursor.fetchall():
            friends.append(
                {"id": row[0],
                 "firstName": row[1],
                 "lastName": row[2],
                 "telephone": row[3],
                 "email": row[4],
                 "notes": row[5]})
        return friends


    def friend(self, id: str) -> dict:
        """
        Return data on a specific friend.

        Args:
            id: The unique identifier of a specific friend.

        Returns:
            A dict of data on the specified friend.

        Raises:
            ValueError: If no matching friend is found.
        """
        cursor = self.connection.execute(
            'SELECT id, firstName, lastName, telephone, email, notes '
            'FROM friends '
            'WHERE lower(id) = ?', [id.lower()])
=======

class Datastore:
    """
    Provides an interface to an SQLite database and associated methods.
    """

    def __init__(self):
        self.connection = sqlite3.connect("/tmp/friends.db")

    def friends(self) -> dict:
        """
        Return a representation of all rows in the friends table.

        Returns
            A JSON ready dictionary representing all rows of the friends table.
        """
        cursor = self.connection.execute(
            'select id, firstName, lastName, telephone, email, notes '
            'from friends')

        friends_collection = list()
        for friend_row in cursor.fetchall():
            friends_collection.append(
                {"id": friend_row[0],
                 "firstName": friend_row[1],
                 "lastName": friend_row[2],
                 "telephone": friend_row[3],
                 "email": friend_row[4],
                 "notes": friend_row[5]})

        return friends_collection

    def friend(self, id: str) -> dict:
        """
        Obtain a specific friend record and return a representation of it.

        Args:
            id (str): An `id` value which will be used to find a specific
                datastore row.

        Returns
            A JSON ready dictionary representing a specific
            row of the friends table.
        """
        cursor = self.connection.execute(
            'select id, firstName, lastName, telephone, email, notes '
            'from friends where lower(id) = ?',
            [id.lower()])
>>>>>>> proposed-changes

        friend_row = cursor.fetchone()

        if friend_row:
<<<<<<< HEAD
            return {"id": friend_row[0],
                    "firstName": friend_row[1],
                    "lastName": friend_row[2],
                    "telephone": friend_row[3],
                    "email": friend_row[4],
                    "notes": friend_row[5]}
        else:
            raise ValueError("No friend resource found for id: {}".format(id))


    def create_friend(self, data: dict):
        """
        Create a new friend entry is our datastore of friends.
=======
            return {
                "id": friend_row[0],
                "firstName": friend_row[1],
                "lastName": friend_row[2],
                "telephone": friend_row[3],
                "email": friend_row[4],
                "notes": friend_row[5]}

    def create_friend(self, data: dict):
        """
        Create a new friend record in our database.
>>>>>>> proposed-changes

        Args:
            data: A dictionary of data for our new friend.  Must have
                the following elements: ['id', 'firstName', 'lastName',
                'telephone', 'email', 'notes']

        Raises:
            ValueError: If data is None, doesn't contain all required
<<<<<<< HEAD
                elements, or a duplicate id already exists in `friends`.
=======
                elements, or an existing record with the same id exists
                in the friends table.
>>>>>>> proposed-changes
        """
        if data is None:
            raise ValueError(
                "`None` was received when a dict was expected during "
                "the attempt to create a new friend resource.")

        required_elements = {"id", "firstName", "lastName", "telephone",
                             "email", "notes"}

        if not required_elements.issubset(data):
            raise ValueError("Some of the data required to create a friend "
                             "was not present.  The following elements "
                             "must be present to create a friend: {}".format(
                required_elements))

<<<<<<< HEAD
        for element in data:
            if element not in required_elements:
                data.pop(element)

        try:
            self.friend(data['id'])
        except ValueError:
            self.connection.execute(
                'INSERT into friends (id, firstName, lastName, telephone, email, notes) '
                'VALUES (?, ?, ?, ?, ?, ?)',
                [data['id'],
                 data['firstName'],
                 data['lastName'],
                 data['telephone'],
                 data['email'],
                 data['notes']])
            self.connection.commit()
        else:
            raise ValueError("A friend already exists with the "
                             "`id` specified: {}".format(data['id']))


    def update_friend(self, id: str, data: dict):
        """
        Update an existing friend entry is our datastore of friends.

        Args:
            data: A dictionary of data to update an existing friend entry with.

        Raises:
            ValueError: If data is None or if no matching friend entry is found.
=======
        if self.friend(data['id']):
            raise ValueError(
                "A friend already exists with the `id` specified: {}".format(
                    data['id']))

        self.connection.execute(
            'insert into friends (id, firstName, lastName, telephone, email, notes) '
            'values (?, ?, ?, ?, ?, ?)',
            [data['id'],
             data['firstName'],
             data['lastName'],
             data['telephone'],
             data['email'],
             data['notes']])
        self.connection.commit()

    def update_friend(self, id: str, data: dict):
        """
        Update an existing friend entry is our database.

        Args:
            id: The id value of the friend to update.
            data: A dictionary of data to update an existing friend entry with.

        Raises:
            ValueError: If data is None or if not matching friend entry is found.
>>>>>>> proposed-changes
        """
        if data is None:
            raise ValueError(
                "`None` was received when a dict was expected during "
                "the attempt to update an existing friend resource.")

        required_elements = {"id", "firstName", "lastName", "telephone",
<<<<<<< HEAD
                                 "email", "notes"}
=======
                             "email", "notes"}
>>>>>>> proposed-changes

        if not required_elements.issubset(data):
            raise ValueError("Some of the data required to create a friend "
                             "was not present.  The following elements "
                             "must be present to create a friend: {}".format(
                required_elements))

<<<<<<< HEAD
        try:
            matched_friend = self.friend(id)
        except ValueError:
            raise
        else:
            self.connection.execute(
                'UPDATE friends '
                'SET id=?, firstName=?, lastName=?, telephone=?, email=?, notes=? '
                'WHERE lower(id) = ?',
                [data['id'],
                 data['firstName'],
                 data['lastName'],
                 data['telephone'],
                 data['email'],
                 data['notes'],
                 data['id'].lower()])
            self.connection.commit()

=======
        if not self.friend(id):
            raise ValueError(
                "No existing friend was found matching id: {}".format(id))

        self.connection.execute(
            "UPDATE friends "
            "SET id=?, firstName=?, lastName=?, telephone=?, email=?, notes=? "
            "WHERE lower(id) = ?",
            [data['id'],
             data['firstName'],
             data['lastName'],
             data['telephone'],
             data['email'],
             data['notes'],
             data['id'].lower()])
        self.connection.commit()
>>>>>>> proposed-changes

    def destroy_friend(self, id: str):
        """
        Remove an existing friend entry from our datastore of friends.

        Args:
            id: The id value of the friend to delete.

<<<<<<< HEAD
        Raises:
            ValueError: If the `id` parameter doesn't match any existing
            friend entries in our datastore.

        """
        try:
            matched_friend = self.friend(id)
        except ValueError:
            raise
        else:
            self.connection.execute(
                'DELETE '
                'FROM friends '
                'WHERE lower(id) = ?',
                [id.lower()])
            self.connection.commit()
=======
        Returns:
            ValueError: If the `id` parameter doesn't match any existing
            friend records in our database.

        """
        if self.friend(id):
            cursor = self.connection.execute(
            'DELETE  '
            'from friends where lower(id) = ?',
            [id.lower()])

            if not cursor.rowcount:
                raise ValueError()
            else:
                self.connection.commit()
        else:
            raise ValueError(
                "No existing friend was found matching id: {}".format(id))
>>>>>>> proposed-changes
