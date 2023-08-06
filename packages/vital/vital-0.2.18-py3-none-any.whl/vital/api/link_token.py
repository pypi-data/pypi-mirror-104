from typing import Any, Mapping

from vital.api.api import API

link_token_field_names = [
    "user_key",
]


class LinkToken(API):
    """Endpoints for managing link tokens."""

    def create(self, configs: Mapping[str, Any]) -> Mapping[str, str]:
        """
        Create a Link token.
        :param dict configs: A required dictionary to configure the Link token.
        """

        body = {}

        for field in link_token_field_names:
            body[field] = configs.get(field)

        return self.client.post("/link/token/", body)
