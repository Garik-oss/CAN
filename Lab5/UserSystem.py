class Permission:
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

class Role:
    
    def __init__(self, name):
        self.name = name
        self.permissions = []

    def add_permission(self, permission):
        if permission not in self.permissions:
            self.permissions.append(permission)
    
    def remove_permission(self, permission):
        if permission in self.permissions:
            self.permissions.remove(permission)
    
    def __str__(self):
        return f"Role: {self.name}, Permissions: {', '.join(str(p) for p in self.permissions)}"

class User:

    def __init__(self, username, role):
        self.username = username
        self.role = role
    
    def has_permission(self, permission_name):
        """Check if the user has a specific permission."""
        return any(permission.name == permission_name for permission in self.role.permissions)
    
    def __str__(self):
        return f"User: {self.username}, Role: {self.role.name}"

read_permission = Permission('read')
write_permission = Permission('write')
delete_permission = Permission('delete')
execute_permission = Permission('execute')

admin_role = Role('Admin')
admin_role.add_permission(read_permission)
admin_role.add_permission(write_permission)
admin_role.add_permission(delete_permission)
admin_role.add_permission(execute_permission)

user_role = Role('User')
user_role.add_permission(read_permission)
user_role.add_permission(write_permission)

guest_role = Role('Guest')
guest_role.add_permission(read_permission)

admin_user = User('admin_user', admin_role)
regular_user = User('regular_user', user_role)
guest_user = User('guest_user', guest_role)

print(f"{admin_user} - Has write permission: {admin_user.has_permission('write')}")
print(f"{regular_user} - Has delete permission: {regular_user.has_permission('delete')}")
print(f"{guest_user} - Has read permission: {guest_user.has_permission('read')}")

guest_user.role.add_permission(execute_permission)
print(f"{guest_user} - Has execute permission: {guest_user.has_permission('execute')}")

guest_user.role.remove_permission(read_permission)
print(f"{guest_user} - Has read permission after removal: {guest_user.has_permission('read')}")
