mapping = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

ind_numerical_cnt = ""
total_numerical_cnt = 0
char_cnt = ""

sorted_keys = sorted(mapping.keys(), key=len, reverse=True)
found= False
with open('day1.txt') as f:
    for line in f:
        s = line.strip('\n')
        i = 0
        while i < len(s):
            found = False
            if i < len(s) and s[i].isdigit():
                char_cnt += s[i]
                i += 1
            else:
                for word, digit in mapping.items():
                    if s[i:i+len(word)] == word:
                        char_cnt += mapping[word]
                        i += 1
                        found = True
                if not found:
                    i += 1
        
        # single characters are interpreted as duplicates ie. '7e' is 77
        if len(char_cnt) == 1:
            char_cnt = char_cnt * 2
        elif len(char_cnt) > 2:
            char_cnt = char_cnt[0] + char_cnt[-1]
        
        total_numerical_cnt += int(char_cnt)
        char_cnt = ""
        
    print("The sum of all calibration values: {}".format(total_numerical_cnt))