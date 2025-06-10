x = 10
result = x == 10 #xが10と等しいかどうか？
print(result) #出力はTrue/Falseとなる(Bool式)

a = 10
b = 20
result = a >= b #aはb以上かどうか
print(result)

a = 10
b = 20
result = a < b #aはb未満かどうか
print(result)

x = "A"
result = x in "Apple" #AはAppleに含まれているかどうか
print(result)

x = "apple"
result = x in ["apple", "banana"] 
print(result)

age = 20
gender = "女性"
result = (age >= 20) and (gender == "女性") #どちらも条件を満たしている場合→True
print(result)

age = 20
gender = "女性"
result = (age >= 20) or (gender == "女性") #どちらかが条件を満たしていれば→True
print(result)

age = 20
gender = "女性"
result = (age >= 20) or (gender == "女性") #どちらかが条件を満たしていれば→True
print(result)

age = 20
gender = "女性"
result = not (age >= 20)  #notの否定系〜でなければ
print(result)
