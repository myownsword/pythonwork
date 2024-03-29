import asyncio
import orm
import random

from www.models import User


async def test(loop):
    await orm.create_pool(loop,user='root',password='Pwd_2019',db='awesome')
    u =User(name='test',email='test%s@example.com' % random.randint(0,10000000),passwd='abc123456',image='about:blank',admin=True)
    await u.save()


#要运行协程，需要使用事件循环
if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test(loop))
        print('Test finished.')
        loop.close()



