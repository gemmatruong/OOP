
class MyString:
    def __init__(self, s):
        self.string = s
        self.length = self.len()

    def __str__(self):
        return self.string

    def print(self):
        print(self.string)

    def len(self):
        count = 0
        for char in self.string:
            count += 1
        return count

    def add_string(self, other):
        self.string = '{}{}'.format(self.string, other)
        return self

    def substring(self, start, end):
        if start > end:
            return ''

        substr = ''
        for i in range(start, end):
            if i >= self.length:
                break
            substr = MyString(substr)
            substr = substr.add_string(self.string[i])
        return substr

    def insert_string(self, pos, other):
        if pos > self.length:
            return "Position is exceed the length of string"

        st_part = self.substring(0, pos)
        last_part = self.substring(pos, self.length)
        st_part = MyString(st_part)
        ins_str = MyString(st_part.add_string(other)).add_string(last_part)
        return ins_str

    def delete_string(self, start, end):
        if start > end:
            return "Invalid input"

        st_part = self.substring(0, start)
        last_part = self.substring(end, self.length)

        st_part = MyString(st_part)
        del_str = st_part.add_string(last_part)
        return del_str

    def replace_string(self, start, end, other):
        if start > end:
            return self.string

        steps = end - start
        st_part = self.substring(0, start)
        last_part = self.substring(end, self.length)
        st_part = MyString(st_part)

        other = MyString(other)
        if end < self.length:
            added_part = other.substring(0, steps)
        else:
            added_part = other.substring(0, self.length-start)

        r_str = MyString(st_part.add_string(added_part)).add_string(last_part)
        return r_str


    def return_string(self):
        return '{}'.format(self.string)
    
    # def find_string(self, start, chars):
    #     if start < 0 or start > self.length:
    #         return 'Out of length'
        
    #     for i in range(start,self.length):
    #         for j in range(0,MyString(chars).len()):
    #             if self.string[i] == chars[j]


str1 = 'Hello Gemma!'

# str1.print()
print(MyString(str1).len())                               # 12
print(MyString(str1).add_string(' Nice to meet you.'))    # Hello Gemma! Nice to meet you.

# print('---------------------------')
print(MyString(str1).substring(2,4))          # ll
print(MyString(str1).substring(0,1))          # H
print(MyString(str1).substring(1,1))          # 
print(MyString(str1).substring(4,1))          # 
print(MyString(str1).substring(4,18))         # o Gemma!
print(MyString(str1).substring(16,19))        # 

print('---------------------------')
print(MyString(str1).insert_string(1,'!'))    # H!ello Gemma!
print(MyString(str1).insert_string(0,'X'))    # XHello Gemma!
print(MyString(str1).insert_string(0,''))     # Hello Gemma!
print(MyString(str1).insert_string(15,'Y'))   # Position is exceed the length of string

print('---------------------------')
print(MyString(str1).delete_string(0,2))      # llo Gemma!
print(MyString(str1).delete_string(0,12))     # 
print(MyString(str1).delete_string(0,1))      # ello Gemma!
print(MyString(str1).delete_string(11,12))    # Hello Gemma
print(MyString(str1).delete_string(11,11))    # Hello Gemma!
print(MyString(str1).delete_string(9,16))     # Hello Gem
print(MyString(str1).delete_string(15,16))    # Hello Gemma!
print(MyString(str1).delete_string(5,0))      # Invalid input

print('---------------------------')
print(MyString(str1).replace_string(0,2,'ABCD'))      # ABllo Gemma!
print(MyString(str1).replace_string(1,3,'ABCD'))      # HABlo Gemma!
print(MyString(str1).replace_string(11,12,'ABCD'))    # Hello GemmaA
print(MyString(str1).replace_string(11,11,'ABCD'))    # Hello Gemma!
print(MyString(str1).replace_string(9,16,'ABCD'))     # Hello GemABC
print(MyString(str1).replace_string(15,16,'ABCD'))    # Hello Gemma!

print('---------------------------')
# print(MyString(str1).find_string(0,'ll'))     # True
# print(str1.find_string(8,'G'))      # False
# print(str1.find_string(4,'Gemma'))  # True
# print(str1.find_string(16,'G'))     # Out of length
