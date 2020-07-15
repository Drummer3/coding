from fbchat import Client
from fbchat.models import Message

username = "+995591080888"
password = "Hf384vE?"
client = Client(username, password)

#სალომეს id
thread_id='100004441952367'

# # # # # #

msg = f"256 ხარისხად 256 = {256**256}"
client.send(Message(text=msg), thread_id=thread_id)

# # # # # #

client.logout()