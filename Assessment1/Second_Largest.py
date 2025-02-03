# Input values to add into the list
num = list(map(int, input("Enter numbers in list: ").split()))

def second_largest(num):
    unique_num = list(set(num))  
    if len(unique_num) < 2:
        return None  
    unique_num.sort(reverse=True)  # Sort in descending order
    return unique_num[1]  

# locate and print the 2nd largest number
second_lar = second_largest(num)
if second_largest is None:
    print("Insufficient Data")
else:
    print(f"Second largest number: {second_lar}")