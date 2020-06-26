# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):

    # -----------------------------way1
    #     tail = None
    #     while head is not None:
    #         current = head
    #         head = head.next
    #         current.next = tail
    #         tail = current
    #     return tail

    # ------------------------------way2

        if head is None or head.next is None:
            return head
        tmp_Node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tmp_Node



def main():

    in_data = [1, 2, 3]

    head = ListNode(None)
    last = head
    for value in in_data:
        current = ListNode(value)
        last.next = current
        last = current
    s = Solution()
    res = s.reverseList(head.next)
    print('hello')



if __name__ == '__main__':
    main()
