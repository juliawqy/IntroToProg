#Q1

day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

line12 = "Twelve drummers drumming"
line11 = "Eleven pipers piping"
line10 = "Ten lords a-leaping"
line9 = "Nine ladies dancing"
line8 = "Eight maids a-milking"
line7 = "Seven swans a-swimming"
line6 = "Six geese a-laying"
line5 = "Five gold rings"
line4 = "Four colly birds"
line3 = "Three French hens"
line2 = "Two turtle doves, and"
line1 = "A partridge in a pear tree \n"

lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12]

for n in range(0, 12):
    print(f"On the {day[n]} of Christmas my true love sent to me")
    print(lines[n])
    def lineprint(n):
        if n-1 >= 0:
            print(lines[n-1])
            return n-1
        else:
            return n
    for i in range(0,12):
        n = lineprint(n)

        
    