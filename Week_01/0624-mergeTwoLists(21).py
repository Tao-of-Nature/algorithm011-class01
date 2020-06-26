# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):

        # --------------------------way1
        # l1_data = []
        # while l1 is not None:
        #     l1_data.append(l1.val)
        #     l1 = l1.next
        #
        # l2_data = []
        # while l2 is not None:
        #     l2_data.append(l2.val)
        #     l2 = l2.next
        #
        # l_data = l1_data + l2_data
        # l_data.sort()
        #
        # head = ListNode(None)
        # last = head
        # for value in l_data:
        #     current = ListNode(value)
        #     last.next = current
        #     last = current
        #
        # return head.next

        # -----------------------------way2

        # head = ListNode(None)
        # last = head
        # while l2 or l1:
        #     if l1 is None:
        #         last.next = l2
        #         break
        #     if l2 is None:
        #         last.next = l1
        #         break
        #
        #     if l1.val < l2.val:
        #         last.next = l1
        #         last = l1
        #         l1 = l1.next
        #     else:
        #         last.next = l2
        #         last = l2
        #         l2 = l2.next
        # return head.next

        # ------------------------------way3

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


def main():

    in_data1 = [1, 2, 4]
    in_data2 = [1, 3, 4]

    head1 = ListNode(None)
    last = head1
    for value in in_data1:
        current = ListNode(value)
        last.next = current
        last = current

    head2 = ListNode(None)
    last = head2
    for value in in_data2:
        current = ListNode(value)
        last.next = current
        last = current

    s = Solution()
    res = s.mergeTwoLists(head1.next, head2.next)
    print('hello')



if __name__ == '__main__':
    main()
