default_scopes = {
    "thesis:view-mine": "View my thesis information",
    "subject-material:view-mine": "View my subject-material information",
}

system_scopes = {
    "admin:thesis:view": "View thesis",
    "admin:thesis:edit": "Edit thesis",
    "admin:subject-materials:view": "View subject-materials",
    "admin:subject-materials:edit": "Edit subject-materials",
}

approvable_scopes = {
    "thesis:edit-mine": "Edit my thesis information",
    "subject-material:edit-mine": "Edit my subject-material information",
}

client_scopes = {}
client_scopes.update(default_scopes)
client_scopes.update(approvable_scopes)
scopes = {}
scopes.update(client_scopes)
scopes.update(system_scopes)
