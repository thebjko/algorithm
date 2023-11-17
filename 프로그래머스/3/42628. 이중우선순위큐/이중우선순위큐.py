from dataclasses import dataclass


@dataclass
class Node:
    value: int
    min_index: int
    max_index: int
        
    def __init__(self, value, index):
        self.value = value
        self.min_index = self.max_index = index

    def __gt__(self, other_node):
        return self.value > other_node.value

    def __lt__(self, other_node):
        return self.value < other_node.value

    def __str__(self):
        return str(self.value)


class Heap:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def _left_child(self, index):
        return index * 2 + 1
    
    def _right_child(self, index):
        return index * 2 + 2
    
    def _parent(self, index):
        return (index - 1) // 2

    def insert(self, value):
        cur_min_idx = cur_max_idx = len(self.min_heap)
        node = Node(value, cur_max_idx)
        self.min_heap.append(node)
        self.max_heap.append(node)

        while cur_max_idx and self.max_heap[cur_max_idx] > self.max_heap[self._parent(cur_max_idx)]:
            self._max_swap(cur_max_idx, self._parent(cur_max_idx))
            cur_max_idx = self._parent(cur_max_idx)
    
        while cur_min_idx and self.min_heap[cur_min_idx] < self.min_heap[self._parent(cur_min_idx)]:
            self._min_swap(cur_min_idx, self._parent(cur_min_idx))
            cur_min_idx = self._parent(cur_min_idx)
    
    def _max_swap(self, idx1, idx2):
        self.max_heap[idx1], self.max_heap[idx2] = self.max_heap[idx2], self.max_heap[idx1]
        self.max_heap[idx1].max_index = idx1
        self.max_heap[idx2].max_index = idx2

    def _min_swap(self, idx1, idx2):
        self.min_heap[idx1], self.min_heap[idx2] = self.min_heap[idx2], self.min_heap[idx1]
        self.min_heap[idx1].min_index = idx1
        self.min_heap[idx2].min_index = idx2
    
    def remove_max(self):
        '''match case 구문도 안되네'''
        if len(self.max_heap) == 0:
            return None
        elif len(self.max_heap) == 1:
            self.min_heap.pop()
            return self.max_heap.pop()

        max_node = self.max_heap[0]
        self.max_heap[0] = self.max_heap.pop()
        self.max_heap[0].max_index = 0

        min_index = max_node.min_index
        if min_index < len(self.min_heap) - 1:
            self.min_heap[min_index] = self.min_heap.pop()
            self.min_heap[min_index].min_index = min_index
            self._sink_min_down(min_index)
        elif min_index == len(self.min_heap) - 1:
            self.min_heap.pop()

        self._sink_max_down(0)
        return max_node

    def remove_min(self):
        if len(self.min_heap) == 0:
            return None
        elif len(self.min_heap) == 1:
            self.max_heap.pop()
            return self.min_heap.pop()

        min_node = self.min_heap[0]
        self.min_heap[0] = self.min_heap.pop()
        self.min_heap[0].min_index = 0

        max_index = min_node.max_index
        if max_index < len(self.max_heap) - 1:
            self.max_heap[max_index] = self.max_heap.pop()
            self.max_heap[max_index].max_index = max_index
            self._sink_max_down(max_index)
        elif max_index == len(self.max_heap) - 1:
            self.max_heap.pop()

        self._sink_min_down(0)
        return min_node

    def _sink_max_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            if left_index < len(self.max_heap) and self.max_heap[max_index] < self.max_heap[left_index]:
                max_index = left_index
            if right_index < len(self.max_heap) and self.max_heap[max_index] < self.max_heap[right_index]:
                max_index = right_index
            if max_index != index:
                self._max_swap(index, max_index)
                index = max_index
            else:
                return
    
    def _sink_min_down(self, index):
        min_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            if left_index < len(self.min_heap) and self.min_heap[min_index] > self.min_heap[left_index]:
                min_index = left_index
            if right_index < len(self.min_heap) and self.min_heap[min_index] > self.min_heap[right_index]:
                min_index = right_index
            if min_index != index:
                self._min_swap(index, min_index)
                index = min_index
            else:
                return


def solution(operations):
    heap = Heap()
    for op in operations:
        command, value = op.split()
        if command == 'I':
            heap.insert(int(value))
        elif value == '1':
            heap.remove_max()
        elif value == '-1':
            heap.remove_min()
    x, y = heap.remove_max(), heap.remove_min()
    return [x.value, y.value] if x and y else [0, 0]