default_scopes = {
    "department:view-mine": "View my department information",
    "teacher:view-mine": "View my teacher information",
}

system_scopes = {
    "admin:departments:view": "View departments",
    "admin:departments:edit": "Edit departments",
    "admin:teachers:view": "View teachers",
    "admin:teachers:edit": "Edit teachers",
}

approvable_scopes = {
    "department:edit-mine": "Edit my department information",
    "teacher:edit-mine": "Edit my teacher information",
}

client_scopes = {}
client_scopes.update(default_scopes)
client_scopes.update(approvable_scopes)
scopes = {}
scopes.update(client_scopes)
scopes.update(system_scopes)
