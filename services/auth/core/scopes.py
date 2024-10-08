from oauth.scopes import (
    scopes as oauth_scopes,
    system_scopes as oauth_system_scopes,
    default_scopes as oauth_default_scopes,
)

from api_docs.scopes import (
    scopes as api_docs_scopes,
    system_scopes as api_docs_system_scopes,
    default_scopes as api_docs_default_scopes,
)


scopes = {
    **oauth_scopes,
    **api_docs_scopes,
}

default_scopes = {
    **oauth_default_scopes,
    **api_docs_system_scopes,
}

# These scope only available for system apps
system_scopes = {
    **oauth_system_scopes,
    **api_docs_default_scopes,
}