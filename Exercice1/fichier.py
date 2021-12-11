

def main2():
    print("Ceci est directe")

def main3():
    print("Ceci n'est pas directe")

def main():
    print("First Module's Name: {}".format(__name__))

if __name__ == "__main__":
    print("Run Directly")

else: 
    print("Run From IMPORT")

if __name__ == "__main__":
    main()
    main2()

else: 
    main3()
