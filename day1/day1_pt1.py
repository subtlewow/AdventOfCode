new = ""
count = 0
with open('./day1/day1.txt') as f:
    for line in f:
        tmp = list(line.strip('\n'))
        
        for i, char in enumerate(tmp):
            ascii_val = ord(char)
            if (ascii_val >= 48 and ascii_val <= 57):
                if len(new) >= 2:
                    new = str(int(new) // 10)
                new += char
        
        if len(new) == 1:
            new = new * 2
        
        count += int(new)
        new = ""

    # correct output: 54968
    print("The sum of all calibration values: {}".format(count))