# Advent of Code '23

My attempts and approaches to [Advent of Code](https://adventofcode.com/2023/about)

## Day 1

[https://adventofcode.com/2023/day/1](https://adventofcode.com/2023/day/1)

**Task a**

Interpreting numbers using ASCII values

```python
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
```

**Task b**

Interpreting numbers using ASCII values

```python
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
```


## Day 2

[https://adventofcode.com/2023/day/2](https://adventofcode.com/2023/day/2)


## Day 3
[https://adventofcode.com/2023/day/3](https://adventofcode.com/2023/day/3)

spent 3 days doing this one.. 

1. overcomplicated the process of calculating adjacency
2. searching adjacency for gear icons based on number digits found, and struggled with building numbers when it was found not at start
3. was building numbers and performing operations based on indexing.. horrible and confusing approach.

conclusion:
1. could just perform adjacency calculation by indexing row, col by either (-1, 0, +1).
2. number building would happen if adjacency with number spotted and number was different to 0
3. did operations based on finding gear locations, and used the index as the unique key identifier for dict - had this correct in initial approach