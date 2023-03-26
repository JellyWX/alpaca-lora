import json
import os
import sys

DATA_ROOT = sys.argv[1].strip('/')

final = []

for directory in os.listdir(DATA_ROOT):
    print(directory)
    data = []
    for json_file in os.listdir('{}/{}'.format(DATA_ROOT, directory)):
        if json_file.endswith('.json'):
            with open('{}/{}/{}'.format(DATA_ROOT, directory, json_file)) as f:
                chunk = json.load(f)
                if len(chunk['participants']) > 2:
                    continue
                else:
                    data += chunk['messages']

    if len(data) == 0:
        continue

    clustered = []
    data.sort(key=lambda m: m['timestamp_ms'])
    current = data[0]['sender_name'].startswith('Jude')
    components = []

    for message in data:
        if message.get('content') is None or message.get('content') == 'Liked a message':
            continue

        is_us = message['sender_name'].startswith('Jude')
        if is_us != current:
            current = is_us
            if len(components) > 0:
                clustered.append({
                    'message': '\n'.join(components),
                    'me': not is_us
                })

            components = []

        components.append(message['content'])

    if len(clustered) == 0:
        continue

    if clustered[0]['me']:
        clustered = clustered[1:]

    if len(clustered) == 0:
        continue

    if not clustered[-1]['me']:
        clustered = clustered[:-1]

    for paired in zip(clustered[::2], clustered[1::2]):
        final.append({
            'author': directory,
            'sent': paired[0]['message'],
            'responded': paired[1]['message'],
        })

with open(sys.argv[2], 'w') as f:
    json.dump(final, f, indent=4)
