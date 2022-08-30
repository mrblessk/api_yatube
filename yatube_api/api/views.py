from posts.models import Group, Post
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Получение, создание, изменение и удаление постов.
        GET - доуступен всем.
        POST - доступен авторизованным юзерам.
        PUT, PATCH, DELETE - доустпуны только авторам постов.

    Raises:
        IsAuthenticated: создание постов доступно авторизованным юзерам.
        IsAuthorOrReadOnly: изменение и удаление постов доступно автору.

    Returns:
        posts: экземпляр или список постов.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, ]

    def perform_create(self, serializer):
        """Создание поста."""
        return serializer.save(author=self.request.user)


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
        IsAuthenticated: создание комментария доступно авторизованным юзерам.
        IsAuthorOrReadOnly: изменение и удаление комментария доступно автору.

    Returns:
        comments: экземпляр или список комментариев к посту.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, ]

    def get_queryset(self):
        """Получение комментариев поста."""
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        """Создание комментария под постом."""
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
