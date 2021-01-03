def count_substring(string, sub_string):
    result = 0
    for i in range(len(string) - len(sub_string)+1):
        if sub_string == string[i:i+len(sub_string)]:
            result+=1  
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
