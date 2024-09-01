import requests

def fetch_notes(base_url, filters, relays):
    
    url = base_url + "/v0/fetch/notes"
    
    json_payload = {
     "relays": relays,
     "authors": getattr(filters, 'authors', None),
     "tags": getattr(filters, 'tags', None),
     "event_refs": getattr(filters, 'event_refs', None),
     "pubkey_refs": getattr(filters, 'pubkey_refs', None),
     "since": getattr(filters, 'since', None),
     "until": getattr(filters, 'until', None),
     "limit": getattr(filters, 'limit', None)
    }
    
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json = json_payload, headers = headers)
    
    return response.json()

def send_note(base_url, relays, sender_private_key, msg):
    
    url = base_url + "/v0/send/note"
    
    json_payload = {
        "relays": relays,
        'private_key': sender_private_key,
        'text': msg,
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json = json_payload, headers = headers)
    
    return response

def send_dm(base_url, relays, sender_private_key, receiver_public_key, message):
    
    url = base_url + "/v0/send/dm"
    
    json_payload = {
        "relays": relays,
        'private_key': sender_private_key,
        'public_key': receiver_public_key,
        'text': msg,
    }
    
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json = json_payload, headers = headers)
    
    return response

relays = [
    'wss://relay.nostr.band/all',
    'wss://christpill.nostr1.com',
    'wss://lolison.top',
    'wss://merrcurrup.railway.app',
    'wss://nos.lol',
    'wss://purplepag.es',
    'wss://relay.primal.net',
    'wss://yabu.me/v1',
]

base_url = ''
pk = 'nsec'

# class Filter:
#     pass

# filters = Filter()
# filters.authors = ['npub1g5camgwm4kksc8yjx2kpk67xuh0z0zqh8vr0lhzyy6uldvja47vs2e5el9']
# filters.limit = 10

# notes = fetch_notes(base_url, filters, relays)

# for note in notes:
#     print(notes[note]['content'])

#notes = send_note(base_url, relays, pk, msg)