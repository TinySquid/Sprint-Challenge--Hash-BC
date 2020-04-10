#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    # hash_table_remove,
    hash_table_retrieve,
    # hash_table_resize,
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    # Build hash table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Set initial starting point key
    destination = "NONE"
    # Rebuild trip
    for i in range(0, length - 1):
        # Using destination as key, we get the next destination in order
        destination = hash_table_retrieve(hashtable, destination)
        # Add to array
        route[i] = destination

    # Were done :)
    return route
