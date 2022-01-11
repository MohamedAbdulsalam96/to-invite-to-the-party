# hi! My name is: Mohamed Abdulsalam..
#practice cource..
# #challeange (4.3)
"""
Ask how many people the user wants to invite to a party.
 If they enter a number below10, ask for the names and after each name display “[name] has been invited”.
 If they enter a number which is 10 or higher, display the message “Too many people”.
 Upload program to GitHub and write the link?

"""
list_of_people = list()
while true:
    number = input(" How many people do you want to invite to the party ?")
    if n.isdigit():
       n = int(n)
       if 0 < n < 10 :
           for i in range(n) :
                name = input(" host name : ")
                while  not name.isalpha() :
                    name = input( " wrong name ,please enter right host name : ")
                hosts.append(name)
                print(name," has been invited")
           break
       elif n < 1:
           print("the number should be more than 0")
       else :
           print("Too many people ")

    else:
        print("please enter a number")

