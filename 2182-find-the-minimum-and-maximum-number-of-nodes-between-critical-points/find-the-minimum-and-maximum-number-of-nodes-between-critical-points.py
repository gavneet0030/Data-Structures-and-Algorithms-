class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next

        index = 1

        first_critical = -1
        prev_critical = -1

        min_distance = float('inf')
        max_distance = -1

        while curr.next:
            next_node = curr.next

            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                if first_critical == -1:
                    first_critical = index
                else:
                    min_distance = min(
                        min_distance,
                        index - prev_critical
                    )

                    max_distance = index - first_critical

                prev_critical = index

            prev = curr
            curr = curr.next
            index += 1

        if max_distance == -1:
            return [-1, -1]

        return [min_distance, max_distance]