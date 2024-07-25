# privileges.py

class PrivilegeManager:
    PRIVILEGES = {
        'CMD': ['view_records', 'edit_records', 'delete_records', 'assign_privileges'],
        'MO': ['view_records', 'edit_records'],
        'VD': ['view_records'],
        'PAT': ['view_own_records'],
        'NUR': ['view_records', 'edit_records'],
        'SNUR': ['view_records', 'edit_records', 'assign_privileges'],
        'REC': ['view_records', 'edit_records'],
        'LS': ['view_records', 'conduct_tests'],
        'SLS': ['view_records', 'conduct_tests', 'assign_privileges'],
        'VIS': ['view_public_records']
    }

    @staticmethod
    def has_privilege(user, privilege):
        if not user.is_authenticated:
            return False
        user_privileges = PrivilegeManager.PRIVILEGES.get(user.position, [])
        return privilege in user_privileges

    @staticmethod
    def assign_privilege(user, privilege):
        if not user.is_authenticated or not PrivilegeManager.has_privilege(user, 'assign_privileges'):
            return False
        PrivilegeManager.PRIVILEGES[user.position].append(privilege)
        return True
