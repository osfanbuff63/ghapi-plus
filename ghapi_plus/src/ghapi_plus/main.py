# Actions
class Actions():
    """Wraps all GitHub Actions related things in ghapi.

    Attributes:
        token (str): A valid token to the GitHub API.
    """
    def __init__(self):
        """Initializes the module.

        Args:
            token (str): A valid token to the GitHub API. Usually inherited from the class, but if not provided, will fallback to the OS variable $GITHUB_TOKEN.

        Raises:
            TokenError: The token arg was not passed and the OS variable $GITHUB_TOKEN was not set.
        """
        import os
        super().__init__()
        try:
            github_token = self.token
        except:
            try:
                github_token = os.environ("GITHUB_TOKEN")
            except:
                raise TokenError("The token arg was not passed and the OS variable $GITHUB_TOKEN was not set.")
