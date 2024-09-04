#!/usr/bin/env python3
"""
This is the authentication file to authenticate
users
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ The authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        The authentication public method
        Args:
            path(str): this is the url path
            excluded_paths(List): this is the excluded path
        Return:
            - gives bool
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        The authorization header
        Args:
            request(None): the request
        Return:
            - returns string
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        The current user
        Args:
            request(None): the request
        Return:
            - returns User
        """
        return None
