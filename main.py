import asyncio
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("helloworld", "YourName", "一个简单的 Hello World 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """插件初始化"""

    # 注册命令
    @filter.command("countdown")
    async def countdown(self, event: AstrMessageEvent):
        """倒计时 3-2-1-开始"""
        for i in [3, 2, 1, "开始！"]:
            yield event.plain_result(str(i))
            await asyncio.sleep(0.6)  # 每条消息之间等待 1 秒

    async def terminate(self):
        """插件销毁"""
