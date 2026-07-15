import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []

        # Put the first node of every linked list into the heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        tail = dummy

        while heap:

            value, i, node = heapq.heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next