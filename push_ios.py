# Send payload to APNS
import apns


def push(msg):
    pem = 'apns-prod.pem'
    token = msg['udid']
    data = msg['data']
    payload = apns.Payload(data['alert'], data['badge'], data['sid'], data['sj'])
    # payload = {
    #     'aps': {
    #         'alert': "This is Message!",
    #         'sound': 'hello.caf',
    #         'badge': 123456,
    #     },
    #     'cam': 1,
    #     'sid': 'F28E006B438F90F5FD11BDADF64BDB13',
    #     'sj':'This is the title!',
    # }
    return apns.APN(token, payload, pem)

if __name__ == '__main__':
    msg = {
        'data': {'alert':'This is Message!', 'sj':'This is the title!','badge': 123, 'sid':'7EE2CC4340E745C30D36DF8FE90D7897'},
        'udid': 'c0eee2e3741329defb48e61133ca5a6639a2cd5141d8c396e720c509be14c91f',
        'content': 'iostest'
    }
    print push(msg)