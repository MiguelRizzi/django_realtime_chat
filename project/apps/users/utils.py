def user_directory_path(instance, filename):
    return f'img/users/{instance.user.username}/{filename}'