import factory, random
from faker import Faker
fake = Faker()
from api.models import User, Grant

states = [
  'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
  'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
  'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
  'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
  'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'
]
degrees = [
  'High School', 
  'Undergraduate', 
  'Graduate',
  'Trade/Technical'
]
ethnicities = [
  'Black or African American', 
  'American Indian or Alaska Native',
  'Hispanic or Latino',
  'Asian',
  'Native Hawaiian or Other Pacific Islander',
]

class UserFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = User

  first_name = factory.LazyAttribute(lambda x: fake.first_name())
  last_name = factory.LazyAttribute(lambda x: fake.last_name())

class GrantFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Grant

  organization = factory.Faker('company')
  title = factory.LazyAttribute(lambda x: '{} Grant'.format(x.organization))
  amount = factory.LazyAttribute(lambda x: fake.random_int(min=100, max=10000))
  description = factory.LazyAttribute(lambda x: fake.paragraph())
  deadline = factory.LazyAttribute(lambda x: fake.future_date(end_date='+300d'))

  # if random.random() > 0.25:
  #   education = 'All'
  # else:
  #   education = factory.LazyAttribute(lambda x: fake.random_element(elements=degrees))

  # if random.random() > 0.25:
  #   ethnicity = 'All'
  # else:
  #   ethnicity = factory.LazyAttribute(lambda x: fake.random_element(elements=ethnicities))

  # if random.random() > 0.25:
  #   state = 'All'
  # else:
  #   state = factory.LazyAttribute(lambda x: fake.random_element(elements=states))
    
  education = factory.LazyAttribute(lambda x: fake.random_element(elements=degrees))
  ethnicity = factory.LazyAttribute(lambda x: fake.random_element(elements=ethnicities))
  state = factory.LazyAttribute(lambda x: fake.random_element(elements=states))
  women = factory.LazyAttribute(lambda x: fake.boolean(chance_of_getting_true=25))
  lgbt = factory.LazyAttribute(lambda x: fake.boolean(chance_of_getting_true=25))
  veteran = factory.LazyAttribute(lambda x: fake.boolean(chance_of_getting_true=25))
  immigrant = factory.LazyAttribute(lambda x: fake.boolean(chance_of_getting_true=25))
  url = factory.LazyAttribute(lambda x: fake.url())
  image_url = factory.LazyAttribute(lambda x: fake.image_url())