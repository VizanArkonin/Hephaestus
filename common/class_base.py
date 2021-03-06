from datetime import datetime

from Crypto.Cipher import AES

import client.config as config
from common.general import get_time_formatter
from common.logger import Logger


class ClassBase(object):
    """
    This class serves as inheritance base for every other class that will require universal features, like logger,
    decryptor and such.
    """
    def __init__(self, logger_name, logging_level):
        self._logger = Logger(logger_name, logging_level)

    def log(self, level, text):
        """
        A simple bridge-method, used to pass values to instance's logger.

        :param level: String - level of log message
        :param text: String - message itself
        :return: None
        """
        self._logger.log(level, text)

    def get_cipher(self):
        """
        Creates and returns an instance of AESCipher class - wrapper for AES encryption processing.
        :return: AESCipher class instance
        """
        return AESCipher()

    def get_current_datetime_string(self):
        """
        Returns a current datetime stamp, formatted in readable string
        :return: Timestamp string
        """
        return datetime.now().strftime(get_time_formatter())


class AESCipher:
    """
    Operational wrapper for cipher - helps to wrap encrypt/decrypt calls with string data.
    """
    ENCODING = 'utf-8'

    def __init__(self, key=config.BOARD_SERVICE_CONFIG["crypto_key"],
                 initialization_vector=config.BOARD_SERVICE_CONFIG["crypto_iv"]):
        """
        Creates new AES cipher object, used to encrypt and decrypt given strings.

        :param key: String - Cipher Key. For current mode (CFB), it must be 16, 24 or 32 bytes (string characters) long
        (respectively for AES-128, AES-192 or AES-256)
        :param initialization_vector: String - Initialization vector to use for encryption or decryption.
        For current mode (CFB), it MUST be 16 bytes (string characters) long.
        :return: AES Cipher instance
        """
        self.cipher = AES.new(key.encode(), AES.MODE_CFB, initialization_vector.encode())

    def encrypt(self, payload):
        """
        Encrypts the payload and returns resulted byte array

        :param payload: String payload
        :return: Encoded byte array
        """
        return self.cipher.encrypt(bytes(payload, encoding=self.ENCODING))

    def decrypt(self, payload):
        """
        Decrypts byte array into string.

        :param payload: Byte array payload
        :return: String
        """
        return self.cipher.decrypt(payload).decode(self.ENCODING)
