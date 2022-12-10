Sessions in Redis
=================

This applet allows to store the web sessions in Redis.

Configuration
-------------

The storage of sessions in Redis is activated using environment variables.

* ``TELE_SESSION_REDIS`` has to be ``1`` or ``true``
* ``TELE_SESSION_REDIS_HOST`` is the redis hostname (default is ``localhost``)
* ``TELE_SESSION_REDIS_PORT`` is the redis port (default is ``6379``)
* ``TELE_SESSION_REDIS_PASSWORD`` is the password for the AUTH command
  (optional)
* ``TELE_SESSION_REDIS_URL`` is an alternative way to define the Redis server
  address. It's the preferred way when you're using the ``rediss://`` protocol.
* ``TELE_SESSION_REDIS_PREFIX`` is the prefix for the session keys (optional)
* ``TELE_SESSION_REDIS_EXPIRATION`` is the time in seconds before expiration of
  the sessions (default is 7 days)
* ``TELE_SESSION_REDIS_EXPIRATION_ANONYMOUS`` is the time in seconds before expiration of
  the anonymous sessions (default is 3 hours)
* ``TELE_SESSION_REDIS_COPY_EXISTING_FS_SESSIONS`` when ``1`` or ``true`` copies the existing tele sessions from
  the filesystem to redis when starting
* ``TELE_SESSION_REDIS_PURGE_EXISTING_FS_SESSIONS`` when ``1`` or ``true`` deletes the existing tele sessions from
  the filesystem to redis when starting


The keys are set to ``session:<session id>``.
When a prefix is defined, the keys are ``session:<prefix>:<session id>``

This applet must be added in the server wide applets with (``--load`` option):

``--load=web,session_redis``

Limitations
-----------

* The server has to be restarted in order for the sessions to be stored in
  Redis.
* The applet monkey-patch ``tele.http.Root.session_store`` with a custom
  method when the Redis mode is active, so incompatibilities with other applets
  is possible if they do the same.

Preseve Sessions
----------------

In order to preserve sessions when switching to redis run tele with
``TELE_SESSION_REDIS_COPY_EXISTING_FS_SESSIONS=true tele --load session_redis --stop-after-init``
