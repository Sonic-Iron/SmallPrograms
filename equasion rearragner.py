def addition(equasion):

    for a in range(0,equasion.index("=")):
        print(equasion, a)
        if equasion[a] == "+":
            print(equasion)
            equasion.append("-")
            for b in equasion[0:equasion.index("+")]:
                equasion.append(b)
            print(equasion)

def main(equasion, rearrangefor):
    if str(equasion).isalpha == False:
        eval(int(equasion))
        print("The answer is ",equasion)
    elif rearrangefor not in equasion:
        print("Cannot rearrange for that as it is not in the equasion")
    else:
        equasion = list(equasion)
        for a in range(len(equasion)):
            if equasion[a+1].isalpha == True:

        equasion = addition(equasion)
        print(equasion)

main("11+x=3", "x")
