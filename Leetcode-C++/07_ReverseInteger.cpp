#include <cmath> 

class Solution1 {
public:
    int reverse(int x) {
        int ans = 0;
        int sign = (x < 0) ? -1 : 1;
        x = abs(x); // Make x positive for reversal

        while (x > 0) {
            int digit = x % 10;
            x /= 10;

            if (ans > INT_MAX / 10 || (ans == INT_MAX / 10 && digit > 7)) {
                return 0; 
            }

            ans = ans * 10 + digit;
        }

        return ans * sign;
    }
};
