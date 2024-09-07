#!/usr/bin/env python3
"""Basic Authorization class"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:  # noqa
        """
        Extracts base64
        Args:
            authorization_header(str): authorize
        Returns:
            - Returns base64 encoding
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split('Basic ')[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:  # noqa
        """
        decode
        Args:
            base64_authorization_header(str): the args for base64
        Returns:
            - returns decode_base64
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            base64_decode = base64.b64decode(base64_authorization_header)
            return base64_decode.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):  # noqa
        """
        decoded authorization header
        Args:
            decoded_base64_authorization_header(str): parameter
        Return:
            - returns decoded authorization
        """
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        # the number 1 stands for first occurence of ':' in the str
        email, password = decoded_base64_authorization_header.split(':', 1)  # noqa
        return (email, password)

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):  # noqa
        """
        user credentials
        Args:
            user_email(str): user email
            user_pwd(str): user password
        Return:
            - returns user email and password
        """
        if user_email is None or not isinstance(user_email, str and user_pwd is None or not isinstance(user_pwd, str):  # noqa

            try:
                user = User.search({'email':user_email})
            except Exception:
                return None
            
            if len(user) <= 0:
                return None

            if user[0].is_valid_password(user_pwd):
                return user[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user
        Args:
            request(None): request as iput
        Return:
            - teturns User object instance
        """
        auth_header = self.authorization(request)
        base64_req = self.extract_base64_authorization_header(auth_header)
        decode_req = self.decode_base64_authorization_header(base64_req)
        email, password = self.extract_user_credentials(decode_req)
        return self.user_object_from_credentials(email, password)
