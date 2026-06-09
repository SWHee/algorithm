def solution(ineq, eq, n, m):
    cal = ineq + eq
    
    if ">" in cal:
        return 1 if n >= m else 0
    
    if "<" in cal:
        return 1 if n <= m else 0