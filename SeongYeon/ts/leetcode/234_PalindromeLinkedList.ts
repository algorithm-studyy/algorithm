function isPalindrome(head: ListNode | null): boolean {
  const list = [];

  while (head) {
    list.push(head.val);
    head = head.next;
  }

  for (let i = 0; i < list.length; i++) {
    if (list[i] !== list[list.length - i - 1]) return false;
  }

  return true;
}
