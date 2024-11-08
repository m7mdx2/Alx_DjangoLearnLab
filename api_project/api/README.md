"""

API Authentication Guide:
1. Use the `/api-token-auth/` endpoint to retrieve an authentication token by providing username and password.
2. Include the token in the `Authorization` header for subsequent requests:
   Authorization: Token your_token_here
3. Access to certain views is restricted based on the 
`IsAuthenticated` permission class.

"""
