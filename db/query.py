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

    blog1.subscribers.add(u1)
    blog1.subscribers.add(u2)
    blog2.subscribers.add(u2)

    blog1.save()
    blog2.save()

    topic1 = Topic(title="topic1", blog=blog1, author=u1)
    topic2 = Topic(title="topic2_content", blog=blog1, author=u3, created=datetime(2017, 1, 1, tzinfo=UTC))

    topic1.save()
    topic2.save()

    topic1.likes.add(u1)
    topic1.likes.add(u2)
    topic1.likes.add(u3)

    topic1.save()

def edit_all():
    pass


def edit_u1_u2():
    pass


def delete_u1():
    pass


def unsubscribe_u2_from_blogs():
    pass


def get_topic_created_grated():
    pass


def get_topic_title_ended():
    pass


def get_user_with_limit():
    pass


def get_topic_count():
    pass


def get_avg_topic_count():
    pass


def get_blog_that_have_more_than_one_topic():
    pass


def get_topic_by_u1():
    pass


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass


if __name__ == "__main__":
    create()