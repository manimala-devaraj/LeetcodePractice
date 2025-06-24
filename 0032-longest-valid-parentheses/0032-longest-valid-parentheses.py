class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        mal=0

        for i,n in enumerate(s):
            if n=="(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    mal=max(mal, i - st[-1])

        return mal


        


