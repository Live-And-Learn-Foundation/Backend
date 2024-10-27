from oauth.scopes import (
    scopes as oauth_scopes,
    default_scopes as oauth_default_scopes,
    system_scopes as oauth_system_scopes,
)

from .course_scopes import (
    scopes as course_scopes,
    default_scopes as course_default_scopes,
    system_scopes as course_system_scopes,
)
from .department_scope import (
    scopes as department_scopes,
    default_scopes as department_default_scopes,
    system_scopes as department_system_scopes,
)
from .document_scopes import (
    scopes as document_scopes,
    default_scopes as document_default_scopes,
    system_scopes as document_system_scopes,
)
from .student_scopes import (
    scopes as student_scopes,
    default_scopes as student_default_scopes,
    system_scopes as student_system_scopes,
)

scopes = {
    **oauth_scopes,
    **student_scopes,
    **course_scopes,
    **document_scopes,
    **department_scopes,
}

default_scopes = {
    **oauth_default_scopes,
    **student_default_scopes,
    **course_default_scopes,
    **document_default_scopes,
    **department_default_scopes,
}

system_scopes = {
    **oauth_system_scopes,
    **student_system_scopes,
    **course_system_scopes,
    **document_system_scopes,
    **department_system_scopes,
}
