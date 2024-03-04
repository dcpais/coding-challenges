class Solution {
public:
    int climbStairs(int n) {
        /* Function to find number of unique combs
         * of 1 and 2 steps to go up n flights of stairs
         */
        int nUnique = 0;
        
        int y, x;
        if (n % 2 == 0) x = 0;
        else x = 1;
        
                // x = number of single steps
        // y = number of double steps
        for (x = x; x <= n; x += 2) {
            y = (n-x) / 2;
            nUnique += nCr(x + y, x);
            printf("x = %i c = %i\n", x, nUnique);
        }
        
        return nUnique;
    }
        
    int nCr(int n, int r) {
        if (r > n - r) r = n - r;
        long long combinations = 1;
        for (int i = 1; i <= r; i ++) {
            combinations *= n - r + i;
            combinations /= i;
        }
        return (int) combinations;
    }
};