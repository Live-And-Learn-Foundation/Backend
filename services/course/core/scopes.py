from courses.scopes import (
    scopes as courses_scopes,
    default_scopes as courses_default_scopes,
    system_scopes as courses_system_scopes,
)

scopes = {
    **courses_scopes,
}

default_scopes = {
    **courses_default_scopes,
}

system_scopes = {
    **courses_system_scopes,
}
