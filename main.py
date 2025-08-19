import asyncio
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register

@register("qqx5_matching_begins", "Chenzb", "一个简单的 匹配倒计时 插件", "1.1.2")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.trigger_word = "匹配倒计时"  # 默认关键词集合

    async def initialize(self):
        """插件初始化"""

    # 命令触发（保留）
    @filter.command("匹配倒计时")
    async def countdown_command(self, event: AstrMessageEvent):
        await self._do_countdown(event)

    # 消息触发（关键词）
    @filter.event_message_type(filter.EventMessageType.GROUP_MESSAGE)
    async def on_all_message(self, event: AstrMessageEvent):
        text = event.message_str
        if text.strip() == self.trigger_word:
            await self._do_countdown(event)

    # 公共倒计时逻辑
    async def _do_countdown(self, event: AstrMessageEvent):
        for i in [3, 2, 1, "开始！"]:
            await event.send(event.plain_result(str(i)))
            await asyncio.sleep(1)

    # 设置触发词
    @filter.command("设置匹配倒计时触发词")
    async def set_trigger(self, event: AstrMessageEvent, word: str = None):
        # 判断是否为空
        if not word or not word.strip():
            yield event.plain_result("❌ 触发词不能为空，请重新设置。")
            return

        self.trigger_word = word.strip()
        yield event.plain_result(f"✅ 触发词已设置为：{self.trigger_word}")

    async def terminate(self):
        """插件销毁"""
