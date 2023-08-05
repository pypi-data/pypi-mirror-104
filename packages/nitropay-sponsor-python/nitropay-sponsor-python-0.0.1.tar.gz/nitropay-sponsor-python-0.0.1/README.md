# NitroPay Sponsor Library for Python

## Description

Creates a signed token, for passing user identity to sponsor client library.

```python

from nitropay.sponsor import Signer

signer = Signer(private_key)
signed = signer.sign(
    user_id # required
    site_id # required
    name   # optional
    email  # optional
    avatar # optional
)

```
