import asyncio
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register

@register("qqx5_matching_begins", "Chenzb", "一个简单的 匹配倒计时 插件", "1.1.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.trigger_word = "匹配倒计时"  # 默认触发词

    async def initialize(self):
        """插件初始化"""

    # 方式一：命令触发（/匹配倒计时）
    @filter.command("匹配倒计时")
    async def countdown(self, event: AstrMessageEvent):
        """倒计时 3-2-1-开始"""
        await self._do_countdown(event)

    # 方式二：消息关键词触发
    async def on_message(self, event: AstrMessageEvent):
        text = event.message.get_plain_text().strip()
        if text == self.trigger_word:
            await self._do_countdown(event)

    # 公共倒计时逻辑
    async def _do_countdown(self, event: AstrMessageEvent):
        for i in [3, 2, 1, "开始！"]:
            await event.send(event.plain_result(str(i)))
            await asyncio.sleep(1)

    # 提供一个命令修改触发词
    @filter.command("设置匹配倒计时触发词")
    async def set_trigger(self, event: AstrMessageEvent, word: str):
        self.trigger_word = word
        yield event.plain_result(f"触发词已设置为：{word}")

    async def terminate(self):
        """插件销毁"""
