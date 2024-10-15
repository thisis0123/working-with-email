from imap_tools import MailBox

with MailBox("imap.gmail.com").login("email_address","password") as mb:
    #printing all the folders in the email: print(mb.folder.list())
    #printing the current folder: print(mb.folder.get()) by default it is Inbox
    #to get the messages we use a method called fetch: mb.fetch(reverse=True,Make_seen=True)
    #after fetch the messages it is gonna return an iterable object 
    #for message in mb.fetch(reverse=True,Make_seen=True)
    #now you can print whatever you want: print(message.date)
    #print(message.subject)  and so on 
    #there is a search argument as well if you want to get specific messages
    pass