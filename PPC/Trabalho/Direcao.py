from collections import deque

East = deque(maxlen=5)
West = deque(maxlen=5)
Rop = deque(maxlen=4)

len_east = len(East)
len_west = len(West)
lock = False