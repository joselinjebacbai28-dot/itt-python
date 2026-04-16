if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        command_parts = input().split()
        cmd = command_parts[0]
        args = command_parts[1:]
        if cmd == "print":
            print(my_list)
        else:
            getattr(my_list, cmd)(*map(int, args))
