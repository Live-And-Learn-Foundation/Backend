from departments.scopes import (
    scopes as departments_scopes,
    default_scopes as departments_default_scopes,
    system_scopes as departments_system_scopes,
)

scopes = {
    **departments_scopes,
}

default_scopes = {
    **departments_default_scopes,
}

system_scopes = {
    **departments_system_scopes,
}
