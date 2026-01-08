def nested_for():
    arr = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end = " ")
        print()

def nested_while():
    arr = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
    i = 0
    while i < len(arr):
        for j in range(len(arr[i])):
            print(arr[i][j], end = " ")
        print()
        i += 1

if __name__ == "__main__":
    nested_for()
    print()
    nested_while()