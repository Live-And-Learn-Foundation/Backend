from oauth.scopes import (
    scopes as oauth_scopes,
    default_scopes as oauth_default_scopes,
    system_scopes as oauth_system_scopes,
)

from .student_scopes import (
    scopes as student_scopes,
    default_scopes as student_default_scopes,
    system_scopes as student_system_scopes,
)

scopes = {
    **oauth_scopes,
    **student_scopes,
}

default_scopes = {
    **oauth_default_scopes,
    **student_default_scopes,
}

system_scopes = {
    **oauth_system_scopes,
    **student_system_scopes,
}
