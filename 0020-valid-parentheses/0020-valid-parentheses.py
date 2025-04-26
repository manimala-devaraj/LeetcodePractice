class Solution:
    def isValid(self, s: str) -> bool:
        st= []
        map= {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in map:
                top= st.pop() if st else '#'
                if map[i] != top:
                    return False
            else:
                st.append(i)

        return not st
        