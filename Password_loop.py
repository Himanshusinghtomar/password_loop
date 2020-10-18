i = 1
while i <= 10:
    maths = int(input("Enter Your Maths Marks"))
    eng = int(input("Enter Your English Marks"))
    phy = int(input("Enter Your Physics Marks"))
    che = int(input("Enter Your Chemistry Marks"))
    sans = int(input("Enter Your Sanskrit Marks"))

    avg = (maths + eng + phy + che + sans) / 5

    print(avg)

    i = i+1