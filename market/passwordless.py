import pickle
import base64
from market.models import User
from market import db, config
from fido2.server import Fido2Server
from fido2.webauthn import PublicKeyCredentialRpEntity, PublicKeyCredentialUserEntity

rp = PublicKeyCredentialRpEntity(name=config['name'], id=config['host'])
server = Fido2Server(rp)

def cred_to_string(cred):
    return base64.b64encode(pickle.dumps(cred)).decode()

def string_to_cred(s):
    if s is None or s=='':
        return []
    return pickle.loads(base64.b64decode(s))

def reg_begin(username):
    credentials=get_creds(username)
    options, state=server.register_begin(
        PublicKeyCredentialUserEntity(
            id=username.encode(),
            name=username,
            display_name=username,
        ),
        credentials,
        resident_key_requirement='required',
    )

    return dict(options), state

def reg_complete(username, resp_json, state):
    auth_data=server.register_complete(state, resp_json)
    user=User.query.filter_by(username=username).first()
    credentials=get_creds(username)
    credentials.append(auth_data.credential_data)
    pubkey=cred_to_string(credentials)
    user.public_key=pubkey
    db.session.commit()

def auth_begin():
    options, state=server.authenticate_begin()
    return dict(options), state

def get_creds(username):
    credstr=User.query.filter_by(username=username).first().get_pubkey()
    cred=string_to_cred(credstr)
    return cred

def auth_complete(resp_json, state):
    username=resp_json['response']['userHandle']
    username=base64.b64decode(username).decode()
    creds=get_creds(username)
    server.authenticate_complete(state, creds, resp_json)
    return User.query.filter_by(username=username).first()