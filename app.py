# javaScript 처럼 hoisting 기능은 없음, 변수를 사용하고싶으면 반드시 변수를 맨위에 설정해야함
# python 에서는 snake_case 를 사용함

# variable types :
v_string = "Ha young"
# true, false 는 대문자로 시작
v_boolean_t = True
v_boolean_f = False
v_number = 1
v_float = 1.1
v_none = None

print(type(v_string)) # <class 'str'> : string
print(type(v_boolean_f)) # <class 'bool'> : boolean
print(type(v_number)) # <class 'int'> : integer (정수)
print(type(v_float)) # <class 'float'> : float (소수)
print(type(v_none)) # <class 'NoneType'> : None (empty)

# sequence types :
# 1) lst     *mutable
v_list = ["item_1", "item_2", "item_3", "item_4"]

print(type(v_list)) # <class 'list'> : list (변경 가능한 배열)
print(len(v_list)) # length (4)

print (v_list[0])
print (v_list[0:2])

# 2) tuple     *immutable
v_tuple = ("item_1", "item_2", "item_3", "item_4")

print(type(v_tuple)) # <class 'tuple'> : tuple (변경 불가능한 배열)

# 3) dictionary     
v_dict = {
    'name' : 'Ha young',
    'age' : '31',
    'fav_food' : 'pizza'
}

print(v_dict["name"])
v_dict["korean"] = True # 내용 추가 가능

# built in functions
# ex)
print(type(v_number))
n_num = int(v_number)
print(type(n_num))


# if
number = 5
if number > 0 :
    print("number is bigger than 0")
else :
    print("number is smaller than 0")

number_list = [0, 1, 2, 3]
if 1 in number_list :
    print("the number is 1")
elif 2 in number_list:
    print("the number is 2")
elif 3 in number_list:
    print("the number is 3")
else:
    print("the number is 0")

# for
for variable_name in range (0,10):
    print("this is done by for")

data_list = ["data 1", 'data 2', 'data 3']
for data_in_the_list in data_list :
    # print(data_in_the_list)

    # 각각의 data 에 적용됨
    print(data_in_the_list * 3)
