import firebase_admin
from firebase_admin import credentials
from conf.settings import FIREBASE_AUTHENTICATION


class FirebaseAuthentication:

    def authenticate(self):
        """ Authenticate firebase service """
        cred = credentials.Certificate(FIREBASE_AUTHENTICATION)
        firebase_admin.initialize_app(cred)