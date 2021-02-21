# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    ip = input().split()
    try:
        a, b = int(ip[0]), int(ip[1])
        result = a/b
        print(result)
    except ValueError as e:
        print("Error Code:", e)
        # print("Error Code:", e)
    except ZeroDivisionError as e:

        print("Error Code: integer division or modulo by zero")


