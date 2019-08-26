from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    u1 = User(first_name="u1", last_name="u1")
    u2 = User(first_name="u2", last_name="u2")
    u3 = User(first_name="u3", last_name="u3")

    u1.save()
    u2.save()
    u3.save()

    blog1 = Blog(id=None, title="blog1", author=u1)
    blog2 = Blog(id=None, title="blog2", author=u1)

    blog1.save()
    blog2.save()

    blog1.subscribers.add(u1, u2)
    # blog1.subscribers.add(u2)
    blog2.subscribers.add(u2)

    blog1.save()
    blog2.save()

    topic1 = Topic(title="topic1", blog=blog1, author=u1)
    topic2 = Topic(title="topic2_content", blog=blog1, author=u3, created=datetime(2017, 1, 1, tzinfo=UTC))

    topic1.save()
    topic2.save()

    topic1.likes.add(u1, u2, u3)
    # topic1.likes.add(u2)
    # topic1.likes.add(u3)

    topic1.save()


def edit_all():
    users = User.objects.all()

    for user in users:
        user.first_name = "uu1"
        user.save()


def edit_u1_u2():
    users = User.objects.filter(Q(first_name='u1') | Q(first_name='u2'))

    for user in users:
        user.first_name = "uu1"
        user.save()


def delete_u1():
    User.objects.filter(first_name='u1').delete()


def unsubscribe_u2_from_blogs():
    user2 = User.objects.filter(first_name="u2")
    blog_with_user2 = Blog.objects.filter(subscribers__first_name="u2")
    for blog in blog_with_user2:
        for user in user2:
            blog.subscribers.remove(user)


def get_topic_created_grated():
    return Topic.objects.filter(created__gt=datetime.datetime(2018, 1, 1, tzinfo=UTC))


def get_topic_title_ended():
    return Topic.objects.filter(title__endswith='content')


def get_user_with_limit():
    return User.objects.all().order_by("-id")[0:2]


def get_topic_count():
    return Topic.objects.all().values('blog').annotate(total=Count('blog')).order_by('total')


def get_avg_topic_count():
    return Topic.objects.all().values('blog').annotate(total=Count('blog')).aggregate(Avg('total'))


def get_blog_that_have_more_than_one_topic():
    return Topic.objects.values('blog_id').annotate(total=Count('id')).filter(total__gt=1)


def get_topic_by_u1():
    return Topic.objects.select_related('author').filter(author__first_name='u1')


def get_user_that_dont_have_blog():
    return User.objects.filter(blog__isnull=True).values_list('id').order_by('id')


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    return Topic.objects.filter(likes__isnull=True)


if __name__ == "__main__":
    # create()
    pass
