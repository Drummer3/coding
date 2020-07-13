from fbchat import Client
from fbchat.models import Message

# facebook user credentials
username = "username"
password = "password"
# login
client = Client(username, password)

# get 20 users you most recently talked to
users = client.fetchThreadList()

# get the detailed informations about these users
detailed_users = [ list(client.fetchThreadInfo(user.uid).values())[0] for user in users ]

# sort by number of messages
sorted_detailed_users = sorted(detailed_users, key=lambda u: u.message_count, reverse=True)

#the best friend!
best_friend = sorted_detailed_users[0]

# message the best friend!
client.send(Message(text=f"Congratulations {best_friend.name}, you are my best friend with {best_friend.message_count} messages!"),
            thread_id=best_friend.uid)

# get all users you talked to in messenger in your account
all_users = client.fetchAllUsers()

# let's logout
client.logout()