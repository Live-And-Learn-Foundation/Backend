default_scopes = {
    "users:view-mine": "View my account information",
    "users:edit-mine": "Edit my account information",
}

system_scopes = {
    "admin:roles:view": "View  roles",
    "admin:roles:edit": "Edit roles",
    "admin:users:view": "View all users' information",
    "admin:users:edit": "Edit all users' information",
    "admin:applications:view": "View integrated applications",
    "admin:applications:edit": "Edit integrated applications",
}

approvable_scopes = {
    "openid": "OpenID Connect scope",
}

client_scopes = {}
client_scopes.update(default_scopes)
client_scopes.update(approvable_scopes)
scopes = {}
scopes.update(client_scopes)
scopes.update(system_scopes)
