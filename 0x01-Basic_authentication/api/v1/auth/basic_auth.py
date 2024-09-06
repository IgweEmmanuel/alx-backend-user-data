#!/usr/bin/env python3
"""Basic Authorization class"""
from api.v1.auth.auth import Auth


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
        return authorization_header.split('Basic')[1]
