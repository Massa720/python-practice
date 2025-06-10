x = 5
if x >= 10:                 #if文
    print("10以上")
elif x >= 0:
    print("10未満0以上")    
else:
    print("10未満")
    
    
x_list = [100, 190, 2980]    #リスト
for x in x_list:             #For文
    x_yen = str(x) + "円"
    print(x_yen)

 
x_dict = {"apple": 100, "banana": 350}   #辞書→keyとvalueがある
for key, value in x_dict.items():
    text = key + "は" + str(value) + "円です"
    print(text)
    
for x in range(10):
    print(x)
    
   