z = int(input("enter operation i.e. 1(BMI calculator),2(calculator),3(unit converter) "))
if z == 0:
    print("Please select any 1")
else:
    if z == 1:
        user = input("Enter user name: ")
        height = float(input("Input your height in meters: "))
        weight = float(input("Input your weight in kilogram: "))
        f=open("E:\documents\python\Ishan\exp1.txt","a+")
        bmi = round(weight / (height * height), 2)
        f.write("%s "%user)
        f.write("%s"%bmi)
        f.write("\n")
        f.close
    elif z == 2:
        a = 1
        b = 1
        while a != 0 or b != 0:
            a = int(input("enter first number"))
            b = int(input("enter second number"))
            c = int(input("enter operation i.e. 1(addition),2(substraction),3(multiplication),4(division)"))
            if (a and b) == 0:
                print("Zero detected exiting....")

            else:
                if c == 1:
                    d = a + b
                    fp = open("E:\documents\python\Ishan\exp2.txt", "a+")
                    fp.write("sum is: %f" % d)
                    fp.write("\n")
                    fp.close
                elif c == 2:
                    d = a - b
                    fp = open("E:\documents\python\Ishan\exp2.txt", "a+")
                    fp.write("difference is: %f" % d)
                    fp.write("\n")
                    fp.close
                elif c == 3:
                    d = a * b
                    fp = open("E:\documents\python\Ishan\exp2.txt", "a+")
                    fp.write("product is: %f" % d)
                    fp.write("\n")
                    fp.close
                elif c == 4:
                    d = a / b
                    fp = open("E:\documents\python\Ishan\exp2.txt", "a+")
                    fp.write("on division: %f" % d)
                    fp.write("\n")
                    fp.close
                else:
                    print("invalid entry")
    elif z == 3:
        c = input("Enter the string in which you want to convert : ")
        d = 0
        f = open("E:\documents\python\Ishan\cin.txt", "r+")
        l = []
        for line in f:
            line = line.split(':')
            line[1] = line[1].split('\n')
            if c == 'INR':
                if line[0] == 'INR':
                    d = float(line[1][0])
                elif line[0] == 'USD':
                    d = float(line[1][0]) / 0.015
                elif line[0] == 'Euro':
                    d = float(line[1][0]) / 0.012
            elif c == 'USD':
                if line[0] == 'INR':
                    d = float(line[1][0]) * 0.015
                elif line[0] == 'USD':
                    d = float(line[1][0])
                elif line[0] == 'Euro':
                    d = float(line[1][0]) / 0.85
            elif c == 'Euro':
                if line[0] == 'INR':
                    d = float(line[1][0]) * 0.012
                elif line[0] == 'USD':
                    d = float(line[1][0]) * 0.85
                elif line[0] == 'Euro':
                    d = float(line[1][0])
            l.append(d)
        f.close()
        fp = open("E:\documents\python\Ishan\cin.txt", "a+")
        for i in l:
            fp.write("%s:" % c)
            fp.write("%f" % i)
            fp.write("\n")
        fp.close()


    else:
        print("invalid entry")
