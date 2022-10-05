x = [2, 3, 5, 9, 3,]
print(x)
summ = 0
for i in range(1, len(x), 2):
    if i % 2 == 1:
        summ += x[i]       
print(f"{x} -> сумма элементов на нечётных позициях: {summ}")