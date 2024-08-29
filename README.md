# Nostr Serverless API

This fork uses Modal (https://modal.com/) instead of AWS fot the deployment of the API. Running `modal deploy modal_deploy.py` will deploy the app and return an endpoint. One change made to the original code is in `relay.py` where:

`policy: RelayPolicy = RelayPolicy()`

Was replaced by:

`policy: RelayPolicy = field(default_factory=RelayPolicy)`

And an additional import of `field` from `dataclasses`. I also deleted files related to the original AWS deployment including the Dockerfile in favor of using Modal's API. Everything else below is from the original README with sections and text removed dealing with deployment to AWS. See also the following resources:

* https://www.youtube.com/watch?v=i1241TceGGc
* https://replit.com/@GaryOKeeffe/NostrServerlessAPIDemo#main.py
* https://replit.com/@GaryOKeeffe/NostrChromaExample3#main.py

## Using the API

<details>
<summary>Details:</summary>
  
Full API documentation is available to Open API standards in this project's `openapi.yaml` file, and is also hosted on [Swagger Hub here](https://app.swaggerhub.com/apis/GARYJOKEEFFE/nostr-serverless_api/0.0.1). We also briefly describe them in this section.

Once you have the base URL, you will be able to reach the following endpoints (with more endpoints to follow soon):

<details>
<summary>Verify the API is running correctly</summary>

**Description**: Publishing a "Running Nostr Serverless API" note from your account to verify everything is set up correctly

**Endpoint**: `/v0/verify`

**HTTP Method**: `POST`

**Objects to be added to the HTTP request**:
- relays = [LIST OF RELAYS OR STRING OF RELAY]
- private_key = [PRIVATE KEY IN NSEC FORMAT]

</details>

<details>
<summary>Send a Public Note</summary>

**Description**: Send a note from your account to a set of relays

**Endpoint**: `/v0/send/note`

**HTTP Method**: `POST`

**Objects to be added to the HTTP request**:
- relays = [LIST OF RELAYS OR STRING OF RELAY]
- private_key = [PRIVATE KEY IN NSEC FORMAT]
- text = [STRING OF YOUR NOTE's CONTENT]

</details>

<details>
<summary>Send a DM</summary>

**Description**: Send a DM from your account to someone else's over a set of relays

**Endpoint**: `/v0/send/dm`

**HTTP Method**: `POST`

**Objects to be added to the HTTP request**:
- relays = [LIST OF RELAYS OR STRING OF RELAY]
- sender_private_key = [PRIVATE KEY IN NSEC FORMAT]
- recipient_public_key = [PRIVATE KEY IN NPUB OR HEX FORMAT]
- text = [STRING OF YOUR NOTE's CONTENT]

</details>

<details>
<summary>Fetch Public Notes</summary>

**Description**: Fetch all notes that meet the filter criteria (filters to be added to request)

**Endpoint**: `/v0/fetch/notes`

**HTTP Method**: `POST`

**Objects that can be added to the HTTP request**:
- authors = [LIST OR STRING OF NPUB OR HEX FORMATTED AUTHOR[S]] 
- relays = [LIST OF RELAYS OR STRING OF RELAY]
- event_refs = [LIST OR STRING OF EVENT REFENENCES]
- pubkey_refs = [LIST OR STRING OF PUB KEY REFENENCES]
- since = [INTEGER OF INTERVAL START]
- until = [INTEGER OF INTERVAL TERMINATION]
- limit = [INTEGER OF #NOTES TO FETCH PER RELAY (Defaults to 2000)]

**Objects included in response**:
- Dictionary of noteIDs wherein each object has the following properties:
   - time_created = [INTEGER OF WHEN NOTE WAS CREATED]
   - content = [STRING REPRESENTING NOTE's CONTENT]
   - author = [AUTHORS PUBLIC KEY IN HEX FORMAT]
   - signature = [STRING OF NOTE SIGNATURE]
   - tags = [JSON BLOB OF NOSTR NOTE TAG OBJECTS]

</details>

We will be pubilshing comprehensive examples in video and text format. Follow me on Nostr (npub10mgeum509kmlayzuvxhkl337zuh4x2knre8ak2uqhpcra80jdttqqvehf6) or on Twitter @garyjokeeffe to stay up-to-date. 

</details>
