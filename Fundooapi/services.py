import boto3
import redis
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.conf import settings
# import FundooApp.settings


class Redis:
    # redisConnection = None

    def __init__(self):
        self.redisConnection = redis.StrictRedis(host=settings.REDIS_HOST,
                                                 port=settings.REDIS_PORT, db=0)

    # method to set the redis key value
    def set(self, key, value):
        try:
            self.redisConnection.set(key, value)  # setting the key value in redis cache
        except ValueError as e:
            return e
        except KeyError as e:
            return e

    # method to get redis key value
    def get(self, key):
        try:
            data = self.redisConnection.get(key)  # returning the redis key value
            return data
        except ValueError as e:
            return e
        except KeyError as e:
            return e

    # method to remove the redis token or key
    def remove(self, key):
        try:
            self.redisConnection.delete(key)  # deleting the key
        except KeyError as e:
            return e
        except ValueError as e:
            return e

    # def hset(self, comment, key, value):  # hset(name, key, value)
    #     # Set key to value within hash name Returns 1 if HSET created a new field, otherwise 0
    #     self.redisConnection.hset(comment, key, value)
    #
    # def get_all(self, para):
    #     return self.redisConnection.hgetall(para)


class Validators:
    def valid(self, username, email):
        try:
            user = User.objects.get(username=username)
            print('user:::', user)
            if user:
                return (
                    {
                        'message': 'Username already exist.',
                        'status': False,
                    }
                )
        except ObjectDoesNotExist:
            if User.objects.filter(email=email).count() > 0:
                return ({
                    'message': 'Email already exist.'
                    , 'status': False,
                })
            else:
                return ({
                    'message': '',  # Valid data
                    'status': True,
                })

# class Bucket:
#     def bucket_list(self):
#         s3 = boto3.client('s3')
#         response = s3.list_buckets()
#         # Output the bucket names
#         print('Existing buckets:')
#         for bucket in response['Buckets']:
#             print(f'  {bucket["Name"]}')
