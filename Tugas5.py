for i in range(0,500,10):
    print(i, end=" ")
print()
print()
for i in range(100,50,-2):
    print(i, end=" ")
print()
print()
for i in range(1,11):
    for k in range(1,11):
        n=i*k
        print(k,end=" ")
print()
i=1
while i <5:
    print(i)
    if i==3:
        break
    i+=1
print()
numbers = [
 951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,  615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,  386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527
]
a =0
while a<len(numbers):
    if numbers [a] %2 !=0:
        print(numbers[a], end =" ")
    if numbers [a] ==553:
        break
    a+=1
print()
print()
total= 0
for i in range(1,20,2):
    total +=i
print("1, +3, +5, +7, +9, +11, +13, +15, +17, +19=", total)
print()
print()
jumlah_hari = int(input("masukan nilai"))
for baris in range(jumlah_hari):
    for kolom in range(baris+1):
        print("*", end="")
    print()
