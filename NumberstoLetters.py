Thousands = {1:'One Thousand',2:'Two Thousand',3:'Three Thousand',4:'Four Thousand',5:'Five Thousand',6:'Six Thousand',7:'Seven Thousand',
             8:'Eight Thousand',9:'Nine Thousand',0:''}
Hundreds = {1:'One Hundred',2:'Two Hundred',3:'Three Hundred',4:'Four Hundred',5:'Five Hundred',6:'Six Hundred',7:'Seven Hundred',
             8:'Eight Hundred',9:'Nine Hundred',0:''}
Tens = {1:'Ten',2:'Twenty',3:'Thirty',4:'Fourty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety',0:''}
Teens = {11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'}
Singles = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',0:''}

Number = input("Please enter any number between 1 and 9999... \n ")
AND = ''

lengthofnum = len(Number)
if lengthofnum == 4:
    AND = ' and '
if lengthofnum == 3:
    Number = '0' + Number
    AND = ' and '
if lengthofnum == 2:
    Number = '00' + Number
if lengthofnum == 1:
    Number = '000' + Number
finished = 'n'
WrittenNum = ''


if lengthofnum == 4:
    first_digit = int(Number[0])
    WrittenNum = Thousands.get(first_digit)
    if Number[1:4] == "000":
        finished = 'y'
if lengthofnum >= 3 and finished != 'y':
    second_digit = int(Number[1])
    WrittenNum = WrittenNum + ' ' + Hundreds.get(second_digit)
    if Number[2:4] == "00":
        finished = 'y'
if lengthofnum >= 2 and finished != 'y':
    third_digit = int(Number[2])
    if third_digit == 1:
        checkteen = int(Number[2:4])
        WrittenNum = WrittenNum + AND + Teens.get(checkteen)
        finished = 'y'
    else:
        WrittenNum = WrittenNum + AND + Tens.get(third_digit)
if lengthofnum >= 1 and finished != 'y':
    fourth_digit = int(Number[3])
    WrittenNum = WrittenNum + ' ' + Singles.get(fourth_digit)

print(WrittenNum)

