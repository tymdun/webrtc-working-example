import aiortc
import socketio

# Config variables: change them to point to your own servers
SIGNALING_SERVER_URL = 'https://tylersweat.com:9999'
TURN_SERVER_URL = 'https://turn.tylersweat.com:3478'
TURN_SERVER_USERNAME = 'rsrr'
TURN_SERVER_CREDENTIAL = 'capstone'

# WebRTC config: you don't have to change this for the example to work
# If you are testing on localhost, you can just use PC_CONFIG = {}
aiortc.RTCIceServer('turn:' + TURN_SERVER_URL + '?transport=udp', username=TURN_SERVER_USERNAME,
                    credential=TURN_SERVER_CREDENTIAL, credentialType='password')
