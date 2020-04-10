#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    # hash_table_remove,
    hash_table_retrieve,
    # hash_table_resize,
)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length == 1:
        # Need length of atleast 2
        return None
    elif length == 2:
        # Only 1 possible answer here
        return (1, 0)

    # 1. Build the hash table where a key is the value, and the value is the index
    for i in range(0, len(weights) - 1):
        hash_table_insert(ht, weights[i], i)
        # 2. Calculate second element by subtracting limit from next index value
        target_key = limit - weights[i + 1]

        # 3. Using that as a key, check if exists and then return the tuple if it does
        if hash_table_retrieve(ht, target_key):
            return (i + 1, hash_table_retrieve(ht, target_key))

    # No matches
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
