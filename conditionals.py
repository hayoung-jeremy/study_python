# if

def plus (a, b):
    if type(a) is int or type(a) is float:
        return a + b
    else:
        return None

print(plus("12", 5))


# elif (else if)
def age_check(age):
    print( f"you are {age}!")
    if age < 18:
        print("아직 미성년자에요")
    elif age == 18:
        print("이제 성인이군요?")
    elif age > 20 and age < 30:
        print("20대군요?")
    else:
        print("이제부턴 아저씨..")

age_check(29)