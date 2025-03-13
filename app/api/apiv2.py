import discord
from discord.ext import commands

import os

intents = discord.Intents.default()
intents.voice_states = True  # ボイスステータスの変更を監視
intents.messages = True

bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_voice_state_update(member, before, after):
    # ボイスチャンネルの入退室を検知
    target_voice_channnel       = "集会所1"     # 対象のボイスチャンネル
    target_text_channel_name    = "参加中"      # 対象のテキストチャンネル

    # 入室イベントの判定
    if before.channel is None and after.channnel is None:
        if after.channel.name == target_voice_channnel:
            # ボイスチャンネルメンバーを取得
            if len(after.channel.members) == 1:
                # 最初の一人目の入室
                text_channel = discord.utils.get(member.guild.text_channels,
                                                 name = target_text_channel_name)
                if text_channel:
                    await text_channel.send(f"@モンハン {member.name} が {target_voice_channnel} に入室しました")

bot.run(os.environ['DISCORD_BOT_TOKEN'])