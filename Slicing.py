"""

Slicing: it 2 different ways 
1) indexing
2) Slice() method


"""
Name = "Vamsi Mamidi"
First_Name =Name[:5] #if you use [0:6] like this
Last_Name = Name[6 : ] # use like [6 : 12]

ReversName = Name[::-1] #[0:12:-1] -1 for reverse


print(First_Name)
print(Last_Name)
print(ReversName)

#Slice()

Website = "https://google.com"
Slice = slice(8,-4)

print(Website[Slice])

My_Name = "Vamsi Mamidi"

s = slice(0,-7)
i = slice(6,None) # None meaning until end

print(My_Name[s])
print(f"my initial is : {My_Name[i]}")