new = ""
count = 0
word_count = 0

mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open('day1.txt') as f:
    # for line in f:
        # tmp = list(line.strip('\n'))
        tmp = "eightwothree"
        key = ""
        
        for char in tmp:
            key += char
            
            if key in mapping:
                tmp = tmp.replace(key, "")
                word_count += mapping[key]
                key = ""
            else:
                for mkey in mapping:
                    if mkey in tmp:
                        tmp = tmp.replace(mkey, "")
                        word_count += mapping[mkey]
                        mkey = ""

                
            
            
        print(tmp, word_count)
        
        # for char in line:
        #     ascii_val = ord(char)
        #     if (48 <= ascii_val <= 57):
        #         if len(new) >= 2:
        #             new = str(int(new) // 10)
        #         new += char
        
        # if len(new) == 1:
        #     new = new * 2
        
        # count += int(new)
        # new = ""

    # print("The sum of all calibration values: {}".format(count))
