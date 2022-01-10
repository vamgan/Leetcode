class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(st for st in s if st.isalnum())
        return s1.lower() == s1[::-1].lower()