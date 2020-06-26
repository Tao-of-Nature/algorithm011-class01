# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):

    # ----------------------------way1
    #     tmp_data = []
    #     while head is not None:
    #         if head not in tmp_data:
    #             tmp_data.append(head)
    #             head = head.next
    #         else:
    #             # index = tmp_data.index(head)
    #             # print('tail connects to node index {}'.format(index))
    #             return head
    #     #
    #     # print('no cycle')
    #     return None


    # ----------------------------way2

        slow = fast = head
        if slow is None:
            return None
        while slow is not None and fast is not None:
            slow = slow.next
            if fast.next is None:
                return None
            else:
                fast = fast.next.next
            if fast is slow:
                break
        if fast != slow:
            return None
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next

        return fast


def main():
    in_data = [3, 2, 0, -4]
    pos = 2

    head = ListNode(None)
    last = head
    for value in in_data:
        current = ListNode(value)
        last.next = current
        last = current

    if pos > -1:
        tmp_head = head.next
        for i in range(pos):
            tmp_head = tmp_head.next
        last.next = tmp_head

    s = Solution()
    res = s.hasCycle(head.next)
    print(res)


if __name__ == '__main__':
    main()
