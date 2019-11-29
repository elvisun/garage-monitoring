from ringcentral import SDK
import os 


def send_message(content):
    RECIPIENT = os.getenv('TARGET_PHONE_NUMBER')
    RINGCENTRAL_CLIENTID = os.getenv('RINGCENTRAL_CLIENTID')
    RINGCENTRAL_CLIENTSECRET = os.environ.get('RINGCENTRAL_CLIENTSECRET')
    RINGCENTRAL_SERVER =  os.environ.get('RINGCENTRAL_SERVER')
    RINGCENTRAL_USERNAME =  os.environ.get('RINGCENTRAL_USERNAME')
    RINGCENTRAL_PASSWORD = os.environ.get('RINGCENTRAL_PASSWORD')
    RINGCENTRAL_EXTENSION =  os.environ.get('RINGCENTRAL_EXTENSION')

    rcsdk = SDK(RINGCENTRAL_CLIENTID, RINGCENTRAL_CLIENTSECRET, RINGCENTRAL_SERVER)
    platform = rcsdk.platform()
    platform.login(RINGCENTRAL_USERNAME, RINGCENTRAL_EXTENSION, RINGCENTRAL_PASSWORD)

    platform.post('/restapi/v1.0/account/~/extension/~/sms',
                {
                    'from' : { 'phoneNumber': RINGCENTRAL_USERNAME },
                    'to'   : [ {'phoneNumber': RECIPIENT} ],
                    'text' : content
                })
