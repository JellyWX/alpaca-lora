import json
import sys

all_messages = []

with open('data-converted/instagram.json') as f:
    all_messages += json.load(f)

with open('data-converted/snap.json') as f:
    all_messages += json.load(f)

# remap authors
AUTHOR_MAP = {
    'andrew-ducks': 'Andrew',
    'jenni_xxxxxx': 'Jenny',
    'sapphirerose3': 'Lily',
    'amani.bvb': 'Amani',
    'xxperfectgirlxx': 'Joanie',
    'tcp180': 'Troy',
    'xchloexrosex': 'Chloe',
    'batrickmahoho': 'Patrick',
    'seanjhatch': 'Sean',
    'dannydan2k13': 'Dan',
    'smithy0705': 'Tom',
    'ruthraistrick': 'Ruth',
    'fayegcxxx': 'Faye',
    'kotharalj': 'Kothar',
    'austin_rigby19': 'Austin',
    'tandillaa': 'Tania',
    'george.staff': 'George',
    'nathan.haine': 'Nathan',
    'drina.an': 'Andrina',
    '532729834788803': 'Jenny',
    'ianfootimmigrationofficer_611473983586522': 'Jenny',
    'meeeennnaaaa_609052373823118': 'Lily',
    'taniabih_569888894409586': 'Tania',
    'tanny_544805120242730': 'Tania',
    'nathan_haine__780617436431355': 'Nathan',
    'tom_m_smith_560902625299646': 'Tom',
    'chloemorris_562176995177952': 'Chloe',
    'ruth_559626702093905': 'Ruth',
    'rorychallinor_550698649655404': 'Rory',
    'andrina_560606428662599': 'Andrina',
    'austinrigby_557319505657958': 'Austin',
    'riley_536698397720069': 'Joanie',
    'faye_572464604147989': 'Faye',
    'seanhatch_542918687108602': 'Sean',
    'patrickmahoney_535569674499608': 'Patrick',
    'jamescraig_433130171410226': 'James',
    'kwthr_427479721975271': 'Kothar',
    'troypriestley_550948809641411': 'Troy',
    'george_568226567905114': 'George',
    'amanix_536967691026473': 'Amani',
}

for message in all_messages:
    if message['author'] in AUTHOR_MAP.keys():
        message['author'] = AUTHOR_MAP[message['author']]
    else:
        message['author'] = None

with open(sys.argv[1], 'w') as f:
    json.dump(all_messages, f, indent=4)
