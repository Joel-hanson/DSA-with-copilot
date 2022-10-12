# This is an implementation of a max heap
from heap import Heap


class MaxHeap(Heap):
    def shift_down(self, i):
        while i < self.size // 2:
            left = 2 * i + 1
            right = 2 * i + 2
            if right < self.size and self.data[right] > self.data[left]:
                left = right
            if self.data[i] >= self.data[left]:
                break
            self.data[i], self.data[left] = self.data[left], self.data[i]
            i = left

    def shift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.data[parent] >= self.data[i]:
                break
            self.data[i], self.data[parent] = self.data[parent], self.data[i]
            i = parent
