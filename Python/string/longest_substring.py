def length_of_longest_substring( s: str):
    substring=""
    for i in range(len(s)):
        if s[i]!=s[i+1]:
            if s[i] not in substring:
                substring+=s[i]
        return substring
print(length_of_longest_substring("abcabcbb"))
    
