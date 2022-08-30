from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    'Permission' уровня объекта.
        Разрешить только владельцам объекта редактировать его.
        Предполагается, что экземпляр модели имеет атрибут 'author'.
    """
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
