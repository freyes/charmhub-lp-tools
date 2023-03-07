import logging

from schema import (
    Hook,
    Optional,
    Regex,
    Schema,
)


_CHARMHUB_NAME = Regex(r'^[a-z][a-z0-9_\-]+$')
_LP_NAME = Regex(r'^[a-z][a-z0-9_\-]+$')
_GIT_BRANCH_NAME = Regex(r'^[a-z][a-z0-9_\-\./]+$')


logger = logging.getLogger(__name__)


class Deprecated(Hook):
    def __init__(self, *args, **kwargs):
        kwargs["handler"] = self._handler
        super().__init__(*args, **kwargs)

    def _handler(self, key, *args):
        logger.warning("`%s` is deprecated. " + (self._error or ""), key)


config_schema = Schema({
    "defaults": {
        "team": str,
        Optional("branches"): {
            _GIT_BRANCH_NAME: {
                Deprecated("build-channels"): object,
                Optional("channels"): [str],
                Optional("enabled", default=True): bool,
                Optional("bases"): [str],
                Optional("duplicate-channels"): [str],
            },
        },
    },
    "projects": [{
        "name": str,
        "charmhub": _CHARMHUB_NAME,
        "launchpad": _LP_NAME,
        "repository": str,
        Optional("team"): str,
        Optional("branches"): {
            _GIT_BRANCH_NAME: {
                Deprecated("build-channels"): dict,
                "channels": [str],
                Optional("enabled", default=True): bool,
                Optional("bases"): [str],
                Optional("duplicate-channels"): [str],
            },
        },
    }],
},
                       ignore_extra_keys=True)
