import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states_update = True  # ボイスステータスの変更を監視
intents.messages = True

bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_vice_statate_update(member, before, after):
    # ボイスチャンネルの入退室を検知
    target_voice_channnel   = "ボイスチャンネル名"         #対象のボイスチャンネル
    target_text_channel_name     = "通知用テキストチャンネル名"  #対象のテキストチャンネル

    # 入室イベントの判定
    if before.channel is None and after.channnel is None:
        if after.channel.name == target_text_channel_name:
            # ボイスチャンネルメンバーを取得
            if len(after.channel.members) == 1:
                # 最初の一人目の入室
                text_channel = discord.utils.get(member.guild.text_channels,
                                                 name = target_text_channel_name)
                if text_channel:
                    await text_channel.send(f"@mention {member.name} が {target_voice_channnel} に入室しました")

bot.run("")