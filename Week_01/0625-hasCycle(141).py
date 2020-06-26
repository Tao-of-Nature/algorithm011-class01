# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):

    # ----------------------------way1
    #     tmp_data = {}
    #     while head is not None:
    #         if head.val not in tmp_data.keys():
    #             tmp_data[head.val] = head
    #         else:
    #             if head is tmp_data[head.val]:
    #                 return True
    #             else:
    #                 tmp_data[head.val] = head
    #         head = head.next
    #     return False


    # ----------------------------way2

        slow = head
        if slow is not None:
            fast = head.next
        else:
            return False
        while slow is not None and fast is not None:
            if fast is slow:
                return True
            slow = slow.next
            if fast.next is None:
                return False
            else:
                fast = fast.next.next

        return False


def main():
    in_data = [3, 2, 0, 3, -4]
    pos = 4

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
