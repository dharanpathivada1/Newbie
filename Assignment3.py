# class Signup:
#     def __init__(self,username,password):
#         self.username=username
#         self.password=password
#     def storeit(self):
#         with open("Signup.txt","w") as file:
#             file.write(f"{self.username} {self.password}")
#             print("account succesffuly created")
# class Login:
#     def __init__(self,username,password):
#         self.username=username
#         self.password=password
#     def saved_data(self):
#         with open("Signup.txt") as file:
#             for i in file:
#                 line=i.split()
#             if line[0]==self.username and line[1] == self.password:
#                 print("you are logged in successfully")

#                 a=int(input("enter 1 if you want to post enter 2 if you want to view/see"))
#                 if a==1:
#                     b=input("Post what ever you want = ")
#                     with open("post.txt","a") as posts:
#                         posts.write("b")
#                 elif a==2:
#                     with open("post.txt") as posts:
#                         for i in posts:
#                            cr= i.strip()
#                            new=cr.replace(" ","\n")
#                            print(new)
#                 else:
#                     print("enter valid input")
#             else:
#                 print("invalid username or password")
                           

    



# def do():
#     z=int(input("enter 1 to login or 2 for sign up"))
#     if z==1:
#         obj1=Login(input("enter the username = "),input("enter the password = "))
#         obj1.saved_data()
#     if z==2:
#         obj2=Signup(input("create the username = "),input("create the password = "))
#         obj2.storeit()
    
#     else:
#        do()
# do()




























class Signup:
        def __init__(self,username,password):
                self.username=username
                self.password=password
        # def store(self):
                with open("database.txt","w") as base:
                    base.write(f"{self.username} {self.password}")
                    print("succesfully sign up")


                






class Login:
        def __init__(self,username,password):
                self.username=username
                self.password=password
        def check(self):
                with open("database.txt") as re:
                        for i in re:
                              lst=i.split()
                        
                        if (self.username==lst[0] and self.password==lst[1]):
                                        print("You are successfully logged in")
                                        d=int(input("if you want to post pres  1  or if you want to view press 2 = "))
                                        if d==1:
                                                with open("post001.txt","a") as po:
                                                        c=input("enter what you want to post = ")
                                                        po.write(f"{c}\n")
                                        if d==2:
                                                with open("post001.txt") as po:
                                                        for i in po:
                                                                i.strip()
                                                                print(i,end="\n")
                        else:
                           print("you entered wrong credintials please try again \n")
                           start()
                                        
                        
                

def start():    
        t= int(input("enter 1 for login /n enter 2 for signup"))
        username=input("Enter the username = ")
        password=input("Enter the password = ")
        if t== 1:
                login=Login(username,password)
                login.check()
        if t==2:
                signup=Signup(username,password)
        else:
                print("try again enter valid choice ")
                start()
start()







