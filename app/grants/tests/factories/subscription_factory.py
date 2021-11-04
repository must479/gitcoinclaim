import factory
from grants.models.subscription import Subscription

from .grant_factory import GrantFactory
from dashboard.tests.factories import ProfileFactory


class SubscriptionFactory(factory.django.DjangoModelFactory):
    """Create mock Subscription for testing."""

    class Meta:
        model = Subscription

    grant = factory.SubFactory(GrantFactory)
    contributor_profile = factory.SubFactory(ProfileFactory)