class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime factorization of t
        temp = t
        req2 = req3 = req5 = req7 = 0
        
        while temp % 2 == 0:
            req2 += 1
            temp //= 2
        while temp % 3 == 0:
            req3 += 1
            temp //= 3
        while temp % 5 == 0:
            req5 += 1
            temp //= 5
        while temp % 7 == 0:
            req7 += 1
            temp //= 7
            
        if temp > 1:
            return "-1"
            
        # Step 2: Precompute minimum digits needed to satisfy powers of 2 and 3
        # dp[a][b] will store the minimum digits needed to gather AT LEAST a factors of 2 and b factors of 3
        dp = [[float('inf')] * 36 for _ in range(55)]
        dp[0][0] = 0
        
        # Forward push phase: Build up counts
        for a in range(55):
            for b in range(36):
                if dp[a][b] == float('inf'):
                    continue
                # Valid digits yielding factors of 2 and 3 are: 2, 3, 4, 6, 8, 9
                for f2, f3 in [(1, 0), (0, 1), (2, 0), (1, 1), (3, 0), (0, 2)]:
                    na = min(54, a + f2)
                    nb = min(35, b + f3)
                    dp[na][nb] = min(dp[na][nb], dp[a][b] + 1)
        
        # Backwards propagation phase: 
        # If we can achieve larger sums in k steps, we can definitely fulfill smaller requirements in k steps
        for a in range(54, -1, -1):
            for b in range(35, -1, -1):
                if a < 54:
                    dp[a][b] = min(dp[a][b], dp[a + 1][b])
                if b < 35:
                    dp[a][b] = min(dp[a][b], dp[a][b + 1])
                    
        def get_min_len(a, b, c, d):
            return c + d + dp[a][b]
            
        digit_factors = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0)
        }
        
        # Prefixes factor accumulations to rapidly verify substrings from `num`
        n = len(num)
        pref2, pref3, pref5, pref7 = [0]*(n+1), [0]*(n+1), [0]*(n+1), [0]*(n+1)
        
        first_zero = n
        for i in range(n):
            if num[i] == '0' and first_zero == n:
                first_zero = i
            d = int(num[i])
            if d > 0:
                f2, f3, f5, f7 = digit_factors[d]
                pref2[i+1] = pref2[i] + f2
                pref3[i+1] = pref3[i] + f3
                pref5[i+1] = pref5[i] + f5
                pref7[i+1] = pref7[i] + f7
                
        # Step 3: Check if the original string works seamlessly as-is
        if first_zero == n:
            if pref2[n] >= req2 and pref3[n] >= req3 and pref5[n] >= req5 and pref7[n] >= req7:
                return num
                
        # Helper sequence constructor dynamically prioritizing smaller integers
        def build_greedy(prefix: str, a, b, c, d_req, total_len) -> str:
            res = list(prefix)
            rem_len = total_len - len(prefix)
            
            while rem_len > 0:
                # Always test from '1' upwards to ensure lexicographical minimum
                for digit in range(1, 10):
                    f2, f3, f5, f7 = digit_factors[digit]
                    na = max(0, a - f2)
                    nb = max(0, b - f3)
                    nc = max(0, c - f5)
                    nd = max(0, d_req - f7)
                    
                    if get_min_len(na, nb, nc, nd) <= (rem_len - 1):
                        res.append(str(digit))
                        a, b, c, d_req = na, nb, nc, nd
                        rem_len -= 1
                        break
            return "".join(res)
            
        # Step 4: Search right-to-left for divergence point (modifying `num` string)
        for i in range(min(n - 1, first_zero), -1, -1):
            rem_a = max(0, req2 - pref2[i])
            rem_b = max(0, req3 - pref3[i])
            rem_c = max(0, req5 - pref5[i])
            rem_d = max(0, req7 - pref7[i])
            
            # Start loop looking for lexicographically lowest next bump up in divergence
            for d in range(int(num[i]) + 1, 10):
                f2, f3, f5, f7 = digit_factors[d]
                na = max(0, rem_a - f2)
                nb = max(0, rem_b - f3)
                nc = max(0, rem_c - f5)
                nd = max(0, rem_d - f7)
                
                # If modifying num string length safely anchors the remaining constraints -> launch reconstruction
                if get_min_len(na, nb, nc, nd) <= (n - 1 - i):
                    return build_greedy(num[:i] + str(d), na, nb, nc, nd, n)
                    
        # Step 5: Failed to fit under equal length, synthesize minimum viable longer bounds 
        new_len = max(n + 1, get_min_len(req2, req3, req5, req7))
        return build_greedy("", req2, req3, req5, req7, new_len)