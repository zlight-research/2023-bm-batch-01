
# Functions in python


# User defined funcetion

# Function without args
def add():
    number_1 = 5 
    number_2 = 6
    value = number_1 + number_2
    print(value)
    return value

result =  add()
print('-----result-----',result)

# Function with args
def join_str(string_1,sting_2):
    value = string_1 +" "+ sting_2
    print("Value :",value)
    return value

result =  join_str("training" , "zlight")
print('-----result-----',result)
    

# Built in funtions

def join_str(string_1 : str = "zlight",sting_2 : str = None):
    value = str(string_1) +" "+ sting_2
    print("Value :",value)
    return value

result =  join_str(sting_2 = "training")
print('-----result-----',result)

