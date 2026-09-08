class Solution {
public:
    int dist(int a, int b) {
        int r1 = a / 6, c1 = a % 6;
        int r2 = b / 6, c2 = b % 6;
        return abs(r1 - r2) + abs(c1 - c2);
    }

    int minimumDistance(string word) {
        const int INF = 1e9;        
        vector<int> dp(26, INF);
        int first = word[0] - 'A';
        for (int f = 0; f < 26; f++)
            dp[f] = 0;
        int cur = first;
        for (int i = 1; i < word.size(); i++) {
            int next = word[i] - 'A';
            vector<int> ndp(26, INF);
            for (int other = 0; other < 26; other++) {
                ndp[other] = min(
                    ndp[other],
                    dp[other] + dist(cur, next)
                );
                ndp[cur] = min(
                    ndp[cur],
                    dp[other] + dist(other, next)
                );
            }

            dp = ndp;
            cur = next;
        }

        return *min_element(dp.begin(), dp.end());
    }
};