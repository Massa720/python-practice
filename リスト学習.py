x = ["a", "b", "c"]
print(x)

x = ["a", "b", "100"]
print(x)

x = []
print(x)

x = ["a", "b", "100"]
print(len(x)) #lenは要素の数を出力させる→3

x = ["a", "b", 100]
print(x[1]) #"b"はインデックス[1]

x = ["a", "b", 100]
x.append("e") #appendは文字列を追加する
print(x)

x = ["a", "b", 100]
x.remove("b") #removeは文字列を削除する
print(x)

x = ["a" , "b", 100]
y = ["e", "f"]
x.extend(y) #extendは２つのリストを結合する
print(x)

x = ["a", "b", "c", "d" ,"e"] #インデックスは左から0,1,2,3,4
print(x[1:4]) #この場合はインデックス1,2,3を出力
    

