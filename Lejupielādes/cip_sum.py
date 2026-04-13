def main():
    skaitlis = int(input("ievadiet veselu skaitli(var būt ļoti gars)"))
    #for i in skaitlis:
    s = str(skaitlis)
    k = [int(c) for c in s]
    viss = sum(k)
    print(viss)

if __name__ == "__main__":
    main()