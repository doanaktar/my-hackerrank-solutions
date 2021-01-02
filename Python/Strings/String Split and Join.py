def split_and_join(line):
    # write your code here
    with_spaces = line.split(" ")
    with_dash = "-".join(with_spaces)
    return with_dash

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
