from django.core.exceptions import PermissionDenied
from posts.models import Group, Post
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Получение, создание, изменение и удаление постов.
        GET - доуступен всем.
        POST - доступен авторизованным юзерам.
        PUT, PATCH, DELETE - доустпуны только авторам постов.

    Raises:
        PermissionDenied: пользователь не является автором поста.

    Returns:
        posts: экземпляр или список постов.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        """Создание поста."""
        return serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """Изменение поста только для автора."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("Изменение чужого контента запрещено!")
        return super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        """Удаление поста только для автора."""
        if serializer.author != self.request.user:
            raise PermissionDenied("Удаление контента запрещено!")
        return super(PostViewSet, self).perform_destroy(serializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение данных о группах.
        GET - доуступен всем.
        PUT, PATCH, DELETE - недоступны.

        Returns:
        groups: список пользовательских групп.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, ]


class CommentViewSet(viewsets.ModelViewSet):
    """Получение, создание, изменение и удаление комментариев.
        GET - доуступен всем.
        POST - доступен авторизованным юзерам.
        PUT, PATCH, DELETE - доустпуны только авторам комментариев.

    Raises:
        PermissionDenied: пользователь не является автором комментария.

    Returns:
        comments: экземпляр или список комментариев к посту.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        """Получение комментариев поста."""
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        """Создание комментария под постом."""
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        """Изменение комментария доступно только автору."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("Изменение чужого контента запрещено!")
        return super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        """Удаление комментария доступно только автору."""
        if serializer.author != self.request.user:
            raise PermissionDenied("Удаление контента запрещено!")
        return super(CommentViewSet, self).perform_destroy(serializer)
