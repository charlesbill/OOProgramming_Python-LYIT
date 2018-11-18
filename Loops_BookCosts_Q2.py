#Book List and cost
book1 = ["The Phoenix Project", 21.99 ]
book2 = ["DevOps Handbook", 15.60 ]
book3 = ["Ansible for Devops", 14.90 ]
book4 = ["Devops for Architects", 38.50 ]
book5 = ["Jenkins 2 - Up and Running", 34.60 ]
myBookList = [book1, book2, book3, book4, book5]
print("BookTitle1                     Cost   Running Total")
counter=0
total=0
while counter <= 4 :
    theBook = myBookList[counter]
    total+= float(theBook[1])
    print("{0:20s} {1:8.2f}        {2:8.2f}".format(theBook[0].ljust(26), theBook[1], total))
    counter+=1
print("The final amount is:  € {0:5.2f}".format(total))
