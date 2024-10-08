default_scopes = {
    "users:view-mine": "View my account information",
    "users:edit-mine": "Edit my account information",
}

system_scopes =  {
    "admin:roles:view": "View  roles",
    "admin:roles:edit": "Edit roles",
    "admin:users:view": "View all users's information",
    "admin:users:edit": "Edit all users's information",
}

scopes = {
    "openid": "OpenID Connect scope",
}

scopes.update(default_scopes);
scopes.update(system_scopes);



