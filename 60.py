for _ in range(int(input())):

    n_a = input()
    set_a = set(map(int, input().split()))
    
    n_b = input()
    set_b = set(map(int, input().split()))
    
    print(set_a.issubset(set_b))
