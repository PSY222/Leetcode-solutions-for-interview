class Solution {
public:
    bool isHappy(int n) {
        if (n < 0) {
            return false;
        }

        long sum = 0;
        while (n != 1 && n != 4) {
            sum = 0;
            while (n > 0) {
                long rem = n % 10;
                sum += rem * rem;
                n /= 10;
            }
            n = sum;
        }

        return n == 1;
    }
};