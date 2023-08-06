
# Stored Secrets handling module in Python

`storedsecrets` is a module implementing a simple approach to keep
your secrets (API keys, passwords, ...) outside of your project files,
so that you can protect them better (e.g. in an encrypted archive, or
any form of external volume), and you don't leak them accidentally
through your favorite versioning tool and platform.

`storedsecrets` exposes a `StoredSecrets` class to handle your secrets.

Typical usage:

    >>> import storedsecrets
    >>> my_secrets = storedsecrets.StoredSecrets("mysecretfile.json")
    >>> API_KEY = my_secrets.get('API_KEY')

If the path of the file is not absolute, it will be searched for in
the directory named in env var `SECRETS`, or in `~/etc/secrets` by
default.

This is minimalist work for the moment.


## Ideas for the future

* make sure all aspects of list / dict are implemented (iterables)

* could be interesting to implement a kind of path (à la XPath) search
  for secrets - `secrets['a/sub/secret']` instead of inelegant
  `secrets['a']['sub']['secret']`.

* get ready for Docker? Allow the use of Docker Secrets?

* manage the "set" operations ? Might not be a good idea, though.


# Track changes

## Changes in 0.1.3

* the `load` function no longer fails silently, but raises the caught
  exception again. This is more pythonic.
  
* a `__getitem__` function has been added, allowing the use of `[]`
  notation to get an element.
