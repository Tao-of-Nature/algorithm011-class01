# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):

        # ----------------------------way1
        # if head is None or head.next is None:
        #     return head
        # res = head.next
        # last = ListNode(None)
        # while head is not None and head.next is not None:
        #     tmp = head.next.next
        #     head, head.next = head.next, head
        #     head.next.next = tmp
        #     last.next = head
        #     last = head.next
        #     head = head.next.next
        #
        # return res

        # ----------------------------------way2

        if head is None or head.next is None:
            return head
        tmp = self.swapPairs(head.next.next)
        head, head.next = head.next, head
        head.next.next = tmp

        return head


def main():

    in_data = [1, 2, 3, 4]

    head = ListNode(None)
    last = head
    for value in in_data:
        current = ListNode(value)
        last.next = current
        last = current
    s = Solution()
    res = s.swapPairs(head.next)
    print('hello')



if __name__ == '__main__':
    main()
