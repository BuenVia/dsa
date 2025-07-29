Traverse has a big O of O(n) because to get every item in the list we have to traverse every item in the list.

Append has a big O of O(n) because to get to the end of the list we have to traverse every item in the list.

Prepend has a big O of O(1) because we only ever need to access the first item in the list regardless of the size of the list.

Insert has a big O of O(n) because the worst case scenario would be to insert a value at the last position on the list and therefore we would need to traverse through the whole list.

Pop first has a big O of 0(1) because we only ever need to access the item at the start of the list regardless of how long the list is.

Pop last has a big O of O(n) because we need to traverse the whole list to get to the last item.

Delete_middle has a big O of O(n) because the worst case scenario could be that we have to travrse the whole list to reach the last item if that is the index given.