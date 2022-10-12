# implementation of heap

# Video for heap sort and heapify algorithm:
# https://www.youtube.com/watch?v=MtQL_ll5KhQ
# https://www.youtube.com/watch?v=cuL8gXCSA58&ab_channel=TECHDOSE


class Heap:
    def __init__(self, data):
        self.data = data
        self.size = len(data)
        self.heapify()

    def heapify(self):
        for i in range(self.size // 2, -1, -1):
            self.shift_down(i)

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

    def insert(self, val):
        self.data.append(val)
        self.size += 1
        self.shift_up(self.size - 1)

    def pop(self):
        self.data[0], self.data[self.size - 1] = self.data[self.size - 1], self.data[0]
        self.size -= 1
        self.shift_down(0)
        return self.data.pop()

    def __str__(self):
        return str(self.data)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    heap = Heap(data)
    print(heap)
    heap.insert(10)
    print(heap)
    heap.pop()
    print(heap)
