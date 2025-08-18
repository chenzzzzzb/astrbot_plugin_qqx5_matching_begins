import asyncio
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register

@register("qqx5_matching_begins", "Chenzb", "一个简单的 匹配倒计时 插件", "1.2.1")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.trigger_words = {"匹配倒计时"}  # 默认关键词集合

    async def initialize(self):
        """插件初始化"""

    # 方式一：命令触发
    @filter.command("匹配倒计时")
    async def countdown_command(self, event: AstrMessageEvent):
        await self._do_countdown(event)

    # 方式二：关键词触发（消息匹配）
    @filter.on_message()   # ✅ 用装饰器监听消息
    async def countdown_keyword(self, event: AstrMessageEvent):
        text = event.message.get_plain_text().strip()
        if text in self.trigger_words:
            await self._do_countdown(event)

    # 公共倒计时逻辑
    async def _do_countdown(self, event: AstrMessageEvent):
        for i in [3, 2, 1, "开始！"]:
            await event.send(event.plain_result(str(i)))
            await asyncio.sleep(1)

    # 设置触发词（可以多个）
    @filter.command("设置触发词")
    async def set_trigger(self, event: AstrMessageEvent, *words: str):
        if not words:
            yield event.plain_result("请提供至少一个触发词")
            return
        self.trigger_words = set(words)
        yield event.plain_result(f"触发词已设置为：{'、'.join(self.trigger_words)}")

    async def terminate(self):
        """插件销毁"""
