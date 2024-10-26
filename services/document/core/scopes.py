from documents.scopes import (
    scopes as documents_scopes,
    default_scopes as documents_default_scopes,
    system_scopes as documents_system_scopes,
)

scopes = {
    **documents_scopes,
}

default_scopes = {
    **documents_default_scopes,
}

system_scopes = {
    **documents_system_scopes,
}
