from collections import deque
from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self):
        result = []
        stack = [self._root]
        while len(stack):
            tmp = stack.pop()
            if not (tmp in result):
                result.append(tmp)
                for t in tmp.outbound[::-1]:
                    stack.append(t)
        return result

    def bfs(self) -> list[Node]:
        result = []
        q = deque()
        q.append(self._root)
        while len(q):
            tmp = q.popleft()
            if not (tmp in result):
                result.append(tmp)
                for t in tmp.outbound:
                    q.append(t)

        return result
