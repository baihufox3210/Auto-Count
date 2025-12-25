import math

def get_sum_of_squares(num: int) -> str | None:
    if num < 0:
        return None
    
    limit = math.isqrt(num) + 1
    
    for i in range(limit):
        i2 = i * i
        if i2 > num: break
        for j in range(i, limit):
            j2 = j * j
            if i2 + j2 > num: break
            for k in range(j, limit):
                k2 = k * k
                if i2 + j2 + k2 > num: break
                for l in range(k, limit):
                    l2 = l * l
                    if i2 + j2 + k2 + l2 == num:
                        # Filter out zeros and format the output
                        parts = [f"{x}²" for x in sorted([i, j, k, l], reverse=True) if x > 0]
                        if not parts and num == 0:
                            return "0²"
                        return "+".join(parts)
                    if i2 + j2 + k2 + l2 > num:
                        break
    return str(num)