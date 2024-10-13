default_scopes = {
    "student:view-mine": "View my student information",
}

system_scopes = {
    "admin:students:view": "View students",
    "admin:students:edit": "Edit students",
}

approvable_scopes = {
    "student:edit-mine": "Edit my student information",
}

client_scopes = {}
client_scopes.update(default_scopes)
client_scopes.update(approvable_scopes)
scopes = {}
scopes.update(client_scopes)
scopes.update(system_scopes)
