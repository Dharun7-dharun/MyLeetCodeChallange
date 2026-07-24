#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (char ch : s) {
            // Push opening brackets
            if (ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);
            }
            // Check closing brackets
            else {
                if (st.empty())
                    return false;

                if ((ch == ')' && st.top() != '(') ||
                    (ch == '}' && st.top() != '{') ||
                    (ch == ']' && st.top() != '['))
                    return false;

                st.pop();
            }
        }

        return st.empty();
    }
};