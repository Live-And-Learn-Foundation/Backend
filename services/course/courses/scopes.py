default_scopes = {
    "course:view-mine": "View my course information",
    "room:view-mine": "View my room information",
    "subject:view-mine": "View my subject information",
}

system_scopes = {
    "admin:courses:view": "View courses",
    "admin:courses:edit": "Edit courses",
    "admin:rooms:view": "View rooms",
    "admin:rooms:edit": "Edit rooms",
    "admin:subjects:view": "View subjects",
    "admin:subjects:edit": "Edit subjects",
}

approvable_scopes = {
    "course:edit-mine": "Edit my course information",
    "room:edit-mine": "Edit my room information",
    "subject:edit-mine": "Edit my subject information",
}

client_scopes = {}
client_scopes.update(default_scopes)
client_scopes.update(approvable_scopes)
scopes = {}
scopes.update(client_scopes)
scopes.update(system_scopes)
