# #Tuples
# ##tuples are imutable
# number = (1,2,3)
# print(number[0])

# #Unpacking
# co = (1,2,3)
# #before unpacking
# x = co[0]
# y = co[1]
# z = co[2]
# #after unpacking
# x , y , z = co
# print(x,y,z)

#Dictionaries 
##no duplicate key value pair
# customer = {
#     "Name": "Rayyan Bey",
#     "Age" : 19,
#     "is_verified": True
# }
# customer["DOB"] = "20 OCT"  #new
# print(customer.get("DOB")) #assigning default value to some unknown key value
#get method gives us NONE when an unknown is printed but [] gives us error

#EXERCISE:
# msg  =  input("Enter message: ")
# words = msg.split(' ')
# emoji = {
#     ":)" : "😄",
#     ":(" : "😔"
# }
# output = ""
# for word in words:
#    output +=  emoji.get(word, word) + " "

# print(output)

