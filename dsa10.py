'''
# Input
name = "Codegnan"
batch = 23
email_id = "saketh@codegnan.com"
print(email_id[7:15])


# Lists --> Mutable collection
email_ids = [
    "saketh@codegnan.com",
    "manasa@codegnan.com",
    "haritha@codegnan.com",
    "support@codegnan.com"
]

# Logic: demonstrate list operations
print(len(email_ids))       
print(email_ids[1])        
print(email_ids[-2])       
print(type(email_ids[-2]))   
print(email_ids[-2:-1])      
print(type(email_ids[-2:-1]))

#store 3 more mailids into above at a time:
email_ids.extend((1,2,4))
print(email_ids)


#Access each mail id one by one -->Loops
for mail in email_ids:
    print(mail)
    print(f'MailId of person is {mail}')
#store the emailids with relevant users names
users = {}
print(type(users))
batches = set()

#get the above email_ids into above users dictionary
users = dict.fromkeys(email_ids)
users['saketh@codegnan.com'] = 2345
print(users)
#All Python built-in data types are built-in functions(int,float, str,list,tuple,set,tuple,dict,bool)
email_ids = [
    "saketh@codegnan.com",
    "manasa@codegnan.com",
    "haritha@codegnan.com",
    "support@codegnan.com"
]

users = {}
print(users)
for i in range(len(email_ids)):
    print(i, email_ids[i])
    users[i+1] = email_ids[i]
    print(users)

#enumerate():it provides by default a counter object(you can store in desired collection).
email_ids = [
    "saketh@codegnan.com",
    "manasa@codegnan.com",
    "haritha@codegnan.com",
    "support@codegnan.com"
]
users = {}
for i in range(len(email_ids)):
    #print(i, email_ids[i])
    users[i+1] = email_ids[i]
    print(users)

data = dict(enumerate(email_ids,1))
print(data)
'''
#python -->object
#functions --> First class objects
#set is a unordered collection as no indexing
