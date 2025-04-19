# main.py

from es_9_11_user import User, Privileges, Admin

admin_user = User("Paperino", "Pepe", "admin", "Paperino@example.com")
admin_privileges = Privileges([
    "can add post",
    "can delete post",
    "can ban user"
])

admin = Admin(admin_user, admin_privileges)

# Call
admin.user.describe_user()
admin.privileges.show_privileges()
