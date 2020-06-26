# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # ------------------------------------way1
    # def reverse_list(self, head):
    #     if head is None or head.next is None:
    #         return head
    #     new_head = self.reverse_list(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return new_head
    #
    # def reverseKGroup(self, head, k):
    #
    #     if head is None or head.next is None:
    #         return head
    #
    #     tail = None
    #     last_tmp_head = ListNode(None)
    #     origin_head = last_tmp_head
    #     while head is not None:
    #         last_head = head
    #         for i in range(k - 1):
    #             head = head.next
    #             if head is None:
    #                 tail = last_head
    #                 break
    #         if tail is not None:
    #             last_tmp_head.next = tail
    #             break
    #         else:
    #             tmp = head.next
    #             head.next = None
    #             head = tmp
    #             tmp_head = self.reverse_list(last_head)
    #             last_tmp_head.next = tmp_head
    #             last_tmp_head = last_head
    #
    #     return origin_head.next

    # ---------------------------------------way2
    # def reverseKGroup(self, head, k):
    #
    #     count = 0
    #     tmp_head = head
    #     while tmp_head is not None:
    #         count += 1
    #         tmp_head = tmp_head.next
    #     times = count // k
    #
    #     hair = ListNode(None)
    #     piece_head = hair
    #     last_tail = piece_tail = head
    #     for _ in range(times):
    #         for _ in range(k):
    #             tmp = head.next
    #             head.next = last_tail
    #             last_tail = head
    #             head = tmp
    #         piece_tail.next = head
    #         piece_head.next = last_tail
    #         piece_head = piece_tail
    #         piece_tail = head
    #     return hair.next

    def reverseKGroup(self, head, k):

        tmp_head = head
        count = 0
        while tmp_head is not None and count < k:
            count += 1
            tmp_head = tmp_head.next

        if count == k:
            piece = self.reverseKGroup(tmp_head, k)
            while count:
                tmp = head.next
                head.next = piece
                piece = head
                head = tmp
                count -= 1
            head = piece
        return head

def main():

    in_data = [1, 2, 3, 4, 5]

    head = ListNode(None)
    last = head
    for value in in_data:
        current = ListNode(value)
        last.next = current
        last = current
    s = Solution()
    res = s.reverseKGroup(head.next, 2)
    print('hello')



if __name__ == '__main__':
    main()
