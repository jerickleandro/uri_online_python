def saudacao(nome, pronome):
    if(pronome == 1):
        print("Hello, Mr. {}!".format(nome))
    elif(pronome == 2):
        print("Hello, Miss {}!".format(nome))
    elif(pronome == 3):
        print("Hello, Mrs. {}!".format(nome))
    elif(pronome == 4):
        print("Hello, Ms. {}!".format(nome))
    else:
        print("What the fuck {}, this is option don't exist".format(nome))

nome = input("Write your name: ")
op = int(input("Which pronoun do you want to be called?\n1-Mr\n2-Miss\n3-Mrs\n4-Ms\n"))
saudacao(nome,op)