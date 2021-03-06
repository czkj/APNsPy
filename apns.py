import socket, ssl, json, struct
import binascii


def Payload(alert='', badge=1, sid = '', sj = ''):
     payload = {
        'aps': {
            'alert': alert,
            'sound': 'hello.aif',
            'badge': badge,
        },
        'cam': 1,
        'sid': sid,
        'sj': sj,
     }
     return payload


def APN(token, payload, theCertfile):
    theHost = ( 'gateway.push.apple.com', 2195 )

    data = json.dumps( payload )

    # Clear out spaces in the device token and convert to hex
    deviceToken = token.replace(' ','')
    byteToken = binascii.unhexlify(token)

    theFormat = '!BH32sH%ds' % len(data)
    theNotification = struct.pack( theFormat, 0, 32, byteToken, len(data), data )

    # Create our connection using the certfile saved locally
    ssl_sock = ssl.wrap_socket(
            socket.socket( socket.AF_INET, socket.SOCK_STREAM ),
            certfile = theCertfile
        )
    ssl_sock.connect( theHost )

    # Write out our data
    ssl_sock.write( theNotification )

    # Close the connection -- apple would prefer that we keep
    # a connection open and push data as needed.
    ssl_sock.close()

    return True
