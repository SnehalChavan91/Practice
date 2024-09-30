def longest_palindromic_substring(s):
    if not s or len(s)==1:
        return s

    def expand_around_center(left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""

    for i in range(len(s)):
        palindrom1 = expand_around_center(i,i)
        palindrom2 = expand_around_center(i,i+1)


        longest=max(longest,palindrom1,palindrom2,key=len)
    return longest

s="babad"
print(longest_palindromic_substring(s))