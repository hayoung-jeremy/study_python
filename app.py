# javaScript 처럼 hoisting 기능은 없음, 변수를 사용하고싶으면 반드시 변수를 맨위에 설정해야함
# print ("Hello" + name)

name = "Ha young"
print (name)


print ("Ha Young"[0])
print ("Ha Young"[0:2])
# 공백도 출력됨
print ("Ha Young"[0:3])

# 배열
car = ['K5','white',5000]

# Dictionary
car2 = {
    'brand':'BMW',
    'model':'520d'
}

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
