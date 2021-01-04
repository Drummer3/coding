from fbchat import Client

username = "username"
password = "password"
client = Client(username, password)

# სალომეს id
salome_id = '100004441952367'
gvantsa_id = '100003324853753'
luka_id = '100006316055945'
# # # # # #

msg = f"ჰელოუ. რომელი საათია?"
# client.send(Message(text=msg), thread_id=thread_id)

# get 20 users you most recently talked to
users = client.fetchThreadList()

# get the detailed informations about these users
detailed_users = [list(client.fetchThreadInfo(user.uid).values())[0] for user in users]

# sort by number of messages
sorted_detailed_users = sorted(detailed_users, key=lambda u: u.message_count, reverse=True)
print(sorted_detailed_users)

# # # # # #

client.logout()