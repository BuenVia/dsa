# Big O Notation

## Linked List

This is based on there being a head and tail.

| Traverse | Prepend | Insert | Append | Pop First | Pop Middle | Pop Last |
|---|---|---|---|---|---|---|
| O(n) | O(1) | O(n) | O(1) | O(1) | O(n) | O(n) |

## Doubly Linked List

This is based on there being a head and tail.

| Traverse | Prepend | Insert | Append | Pop First | Pop Middle | Pop Last |
|---|---|---|---|---|---|---|
| O(n) | O(1) | O(n) | O(1) | O(1) | O(n) | O(1) |

## Stack

| Traverse | Push | Pop | 
|---|---|---|
| O(n) | O(1) | O(1) |

## Queue

| Traverse | Enqueue | Dequeue |
|---|---|---|
| O(n) | O(1) | O(1) |

## Binary Search Tree

The two below operations are `O(log n)` because in each iteration of the `while` loop, we are removing half of the remaining results and thus this is 'divide and conquer'.

However, if the tree was 'unbalanced' this could then lead to the tree degenerating into a linked list, which would therefore turn the Big O into O(n).

| Insert | Contains |
|---|---|
| O(log n) | O(log n) |

## Hash Map

| Hash | Set Hash | Get Hash |
|---|---|---|
| O(1) | O(1) | O(n) |

The `_hash` method is `O(1)` and not `O(n)` because `n` would be the number of items in the hash table, not the number of characters in a string. 

For the 'Get Hash' method, this is O(n) because we are avoid collisions by using 'Separate Chaining' when setting the hash in the Set Hash method. To find the data_map[index] is O(1) but if there is more than 1 item at this index it then becomes O(n) as we will need to loop through the items at this index until we find the relevant item.