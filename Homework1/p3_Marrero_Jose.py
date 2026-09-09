def find_dup_str(s, n):
    for i in range(len(s) - n + 1):
        s1 = s[i:i+n]
        for j in range(i + n, len(s) - n + 1):
            s2 = s[j:j+n]
            if s1 == s2:
                return s1
    return "" 

s = input("Enter s: ")
n = int(input("Enter n: "))
result = find_dup_str(s, n)
print(result)

def find_max_dup(s):
    max_dup = ""

    for n in range(1, len(s) // 2 + 1):
        dup = find_dup_str(s, n)
        if len(dup) != 0:
            max_dup = dup
    return max_dup

s_max = input("Enter s: ")
result_max = find_max_dup(s_max)
print(result_max)
            
