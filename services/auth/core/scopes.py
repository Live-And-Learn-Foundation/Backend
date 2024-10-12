from oauth.scopes import (
    scopes as oauth_scopes,
    default_scopes as oauth_default_scopes,
    system_scopes as oauth_system_scopes,
)

scopes = {
    **oauth_scopes,
}

default_scopes = {
    **oauth_default_scopes,
}

system_scopes = {
    **oauth_system_scopes,
}
