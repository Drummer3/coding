from fbchat import Client
from fbchat.models import Message

username = "+995591080888"
password = "@q$FZ87Yvl"
client = Client(username, password)

#სალომეს id
thread_id='100004441952367'

# # # # # #

msg = f"ჰელოუ. რომელი საათია?"
#client.send(Message(text=msg), thread_id=thread_id)

# get 20 users you most recently talked to
users = client.fetchThreadList()

# get the detailed informations about these users
detailed_users = [ list(client.fetchThreadInfo(user.uid).values())[0] for user in users ]

# sort by number of messages
sorted_detailed_users = sorted(detailed_users, key=lambda u: u.message_count, reverse=True)
print(sorted_detailed_users)

# # # # # #

client.logout()