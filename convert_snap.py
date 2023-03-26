import json
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

chats = {}
conversations = {}

all_messages = sorted(
    filter(
        lambda m: m['Media Type'] == 'TEXT',
        data['Received Saved Chat History'] + data['Sent Saved Chat History']),
    key=lambda m: m['Created']
)

# group conversations
for message in all_messages:
    author = message.get('From') or message.get('To')

    if chats.get(author) is None:
        chats[author] = []

    chats[author].append(message)

# group double-messages
for person, chat in chats.items():
    new_conversation = []
    current = chat[0].get('To') is not None
    components = []

    for message in chat:
        is_to = message.get('To') is not None
        if is_to != current:
            current = is_to
            if len(components) > 0:
                new_conversation.append({
                    'message': '\n'.join(components),
                    'me': not is_to
                })
                components = []

        components.append(message['Text'])

    conversations[person] = new_conversation

final = []
for author, conversation in conversations.items():
    if len(conversation) == 0:
        continue

    if conversation[0]['me']:
        conversation = conversation[1:]

    if len(conversation) == 0:
        continue

    if not conversation[-1]['me']:
        conversation = conversation[:-1]

    for paired in zip(conversation[::2], conversation[1::2]):
        final.append({
            'author': author,
            'sent': paired[0]['message'],
            'responded': paired[1]['message'],
        })

with open(sys.argv[2], 'w') as f:
    json.dump(final, f, indent=4)
