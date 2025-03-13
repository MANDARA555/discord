import discord
import dotenv
import os
from server import server_thread

import asyncio

# 新しいイベントループポリシーを設定
asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
dotenv.load_dotenv()

TOKEN = os.environ['DISCORD_BOT_TOKEN']
intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容の処理
intents.voice_states = True     # ボイスステータスの処理
client = discord.Client(intents=intents)

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

@client.event
async def on_voice_state_update(member, before, after):
    # ボイスチャンネルの入退室を検知
    target_voice_channel       = "集会所1"     # 対象のボイスチャンネル
    target_text_channel_name    = "参加中"      # 対象のテキストチャンネル

    # 入室イベントの判定
    if before.channel is None and after.channel is not None:
        if after.channel.name == target_voice_channel:
            # ボイスチャンネルメンバーを取得
            if len(after.channel.members) == 1:
                # 最初の一人目の入室
                text_channel = discord.utils.get(member.guild.text_channels,
                                                 name = target_text_channel_name)
                if text_channel:
                    # 招待URLの生成
                    invite = await after.channel.create_invite(max_age=19600)
                    await text_channel.send(
                        f"<@&{1280812754458120338}> {member.name} が {target_voice_channel} に入室しました！\n招待URL: {invite.url}"
                    )

# Koyeb用 サーバー立ち上げ
server_thread()
client.run(TOKEN)