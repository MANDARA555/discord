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

@client.event
async def on_voice_state_update(member, before, after):
    # ボイスチャンネルの入退室を検知
    target_voice_channel        = "集会所1"     # 対象のボイスチャンネル
    target_voice_channel2       = "ロビー"     # 対象のボイスチャンネル
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
                    invite = await after.channel.create_invite()
                    await text_channel.send(
                        f"<@&{1343086891808981032}> {member.name} が {target_voice_channel} に入室しました！\n招待URL: {invite.url}"
                    )
        elif after.channel.name == target_voice_channel2:
            # ボイスチャンネルメンバーを取得
            if len(after.channel.members) == 1:
                # 最初の一人目の入室
                text_channel = discord.utils.get(member.guild.text_channels,
                                                 name = target_text_channel_name)
                if text_channel:
                    # 招待URLの生成
                    invite = await after.channel.create_invite()
                    await text_channel.send(
                        f"<@&{1343087023761657897}> {member.name} が {target_voice_channel2} に入室しました！\n招待URL: {invite.url}"
                    )

# Koyeb用 サーバー立ち上げ
server_thread()
client.run(TOKEN)