num = list(map(int, input("Enter numbers in list: ").split()))
a= []
b= []
def Odd_Even(num):
    for i in num:
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    
def main():
    Odd_Even(num)
    print("Even list: ",a)
    print("Odd list: ",b)
main()