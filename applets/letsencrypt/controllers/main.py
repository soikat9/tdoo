
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
import contextlib
import os

from tele import http
from tele.http import request

from ..models.letsencrypt import _get_challenge_dir


class Letsencrypt(http.Controller):
    @http.route("/.well-known/acme-challenge/<filename>", auth="none")
    def acme_challenge(self, filename):
        with contextlib.suppress(IOError):
            with open(os.path.join(_get_challenge_dir(), filename)) as key:
                return key.read()
        return request.not_found()
