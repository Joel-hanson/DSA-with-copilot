# This is an implementation of linkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def deleteNode(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def deleteNodeAtPosition(self, position):
        if self.head == None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    def deleteList(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev

    def getCount(self):

        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def search(self, x):
        current = self.head
        while current != None:
            if current.data == x:
                return True
            current = current.next
        return False

    def getNth(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        assert False
        return 0

    def getNthFromLast(self, n):
        temp = self.head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        if n > length:
            print("Length of the list is less than n")
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        return temp.data

    def getMiddle(self):
        """
        How does this work:
        1. Initialize two pointers, slow and fast
        2. Move slow pointer by one and fast pointer by two
        3. When the fast pointer reaches the end slow pointer will be at the middle
        """
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head is not None:
            while fast_ptr is not None and fast_ptr.next is not None:
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("The middle element is: ", slow_ptr.data)

    def detectLoop(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False

    def removeDuplicates(self):
        curr = self.head
        prev = None
        dup_values = dict()
        while curr:
            if curr.data in dup_values:
                prev.next = curr.next
                curr = None
            else:
                dup_values[curr.data] = 1
                prev = curr
            curr = prev.next

    def swapNodes(self, x, y):
        if x == y:
            return
        prevX = None
        currX = self.head
        while currX and currX.data != x:
            prevX = currX
            currX = currX.next
        prevY = None
        currY = self.head
        while currY and currY.data != y:
            prevY = currY
            currY = currY.next
        if not currX or not currY:
            return
        if prevX:
            prevX.next = currY
        else:
            self.head = currY
        if prevY:
            prevY.next = currX
        else:
            self.head = currX
        currX.next, currY.next = currY.next, currX.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverseUtil(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.reverseUtil(next, curr)

    def reverseRecursive(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

    def rotate(self, k):
        p = self.head
        q = self.head
        prev = None
        count = 0
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        while q:
            prev = q
            q = q.next
        q = prev
        q.next = self.head
        self.head = p.next
        p.next = None

    def moveTailToHead(self):
        if self.head is None or self.head.next is None:
            return
        last = self.head
        second_last = None
        while last.next:
            second_last = last
            last = last.next
        second_last.next = None
        last.next = self.head
        self.head = last

    def sortedInsert(self, new_node):
        current = self.head
        if current is None:
            new_node.next = self.head
            self.head = new_node
        elif current.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            while current.next is not None and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insertSort(self):
        sorted = None
        current = self.head
        while current:
            next = current.next
            self.sortedInsert(current)
            current = next

    def removeLoop(self):
        slow_p = self.head
        fast_p = self.head
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                self.removeLoopUtil(slow_p)
                return 1
        return 0

    def removeLoopUtil(self, loop_node):
        ptr1 = loop_node
        ptr2 = loop_node
        k = 1
        while ptr1.next != ptr2:
            ptr1 = ptr1.next
            k += 1
        ptr1 = self.head
        ptr2 = self.head
        for i in range(k):
            ptr2 = ptr2.next
        while ptr2 != ptr1:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        while ptr2.next != ptr1:
            ptr2 = ptr2.next
        ptr2.next = None

    def pairWiseSwap(self):
        temp = self.head
        while temp and temp.next:
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next

    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0
        while first is not None or second is not None:
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata
            carry = 1 if Sum >= 10 else 0
            Sum = Sum if Sum < 10 else Sum % 10
            temp = Node(Sum)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
        if carry > 0:
            temp.next = Node(carry)

    def isPalindrome(self):
        s = []
        p = self.head
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def deleteAlt(self):
        if self.head is None:
            return
        prev = self.head
        now = prev.next
        while prev is not None and now is not None:
            prev.next = now.next
            now = None
            prev = prev.next
            if prev is not None:
                now = prev.next

    def splitList(self):
        slow_p = self.head
        fast_p = self.head
        if self.head is None:
            return
        while fast_p.next is not None and fast_p.next.next is not None:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
        temp = slow_p.next
        slow_p.next = None
        return temp

    def shuffleMerge(self, a, b):
        dummy = Node(0)
        tail = dummy
        while True:
            if a is None:
                tail.next = b
                break
            if b is None:
                tail.next = a
                break
            tail.next = a
            tail = a
            a = a.next
            tail.next = b
            tail = b
            b = b.next
        self.head = dummy.next

    def sortedMerge(self, a, b):
        result = None
        if a is None:
            return b
        if b is None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def mergeSort(self, h):
        """
        :param h: head of linked list
        :return: head of sorted linked list

        Time Complexity: O(nlogn)

        How does this work?
        1. Find the middle point to divide the list into two halves:
            middle = (l+r)/2
            Call mergeSort for first half:
            Call mergeSort for second half:
        2. Merge the two halves sorted in step 2 and step 3:
            Merge(arr, l, m, r)
        """
        if h is None or h.next is None:
            return h
        middle = self.getMiddle(h)
        nexttomiddle = middle.next
        middle.next = None
        left = self.mergeSort(h)
        right = self.mergeSort(nexttomiddle)
        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def getMiddle(self, head):
        if head is None:
            return head
        slow_p = head
        fast_p = head
        while fast_p.next is not None and fast_p.next.next is not None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
        return slow_p

    def removeDuplicates(self):
        curr = self.head
        if curr is None:
            return
        while curr.next is not None:
            if curr.data == curr.next.data:
                new_next = curr.next.next
                curr.next = None
                curr.next = new_next
            else:
                curr = curr.next

    def moveToFront(self):
        if self.head is None or self.head.next is None:
            return
        secLast = None
        last = self.head
        while last.next is not None:
            secLast = last
            last = last.next
        secLast.next = None
        last.next = self.head
        self.head = last

    def rotate(self, k):
        if k == 0:
            return
        current = self.head
        count = 1
        while count < k and current is not None:
            current = current.next
            count += 1
        if current is None:
            return
        kthNode = current
        while current.next is not None:
            current = current.next
        current.next = self.head
        self.head = kthNode.next
        kthNode.next = None

    def insertMiddle(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        slow_p = self.head
        fast_p = self.head
        if self.head is None:
            return
        while fast_p.next is not None and fast_p.next.next is not None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
        new_node = Node(new_data)
        new_node.next = slow_p.next
        slow_p.next = new_node

    def deleteMiddle(self):
        slow_p = self.head
        fast_p = self.head
        if self.head is None:
            return
        while fast_p.next is not None and fast_p.next.next is not None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
        slow_p.next = slow_p.next.next

    def sortLinkedList(self):
        """
        Time Complexity: O(n^2)
        """
        current = self.head
        index = None
        if self.head is None:
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data
                    index = index.next
                current = current.next
