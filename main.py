import discord
from config import super_secret_token


class MyClient(discord.Client):
    async def on_ready(self, member):
        party_channel_id = 1151092359048724544
        party_channel = client.get_channel(party_channel_id)
        sword_channel_id = 1151755897366904914
        sword_channel = client.get_channel(sword_channel_id)
        if isinstance(party_channel, discord.VoiceChannel):
            if len(party_channel.members) == 0:
                pass
            elif len(party_channel.members) >= 1:
                found_bot = False
                for each_user in party_channel.members:
                    if each_user.id == 1151658242108305539:
                        found_bot = True
                if not found_bot:
                    await party_channel.connect()
                else:
                    voice = member.guild.voice_client
                    await voice.disconnect(force=True)
        if isinstance(sword_channel, discord.VoiceChannel):
            if len(sword_channel.members) == 0:
                pass
            elif len(sword_channel.members) >= 1:
                found_bot = False
                for each_user in sword_channel.members:
                    if each_user.id == 1151658242108305539:
                        found_bot = True
                if not found_bot:
                    await sword_channel.connect()
                else:
                    voice = member.guild.voice_client
                    await voice.disconnect(force=True)

    # async def close(self):
    #    await client.close()
    #    print("Billy Joel has disconnected.")


    async def on_voice_state_update(self, member, before, after):
        found_bot = False
        party_channel_id = 1151092359048724544
        party_channel = client.get_channel(party_channel_id)
        sword_channel_id = 1151755897366904914
        sword_channel = client.get_channel(sword_channel_id)
        if isinstance(party_channel, discord.VoiceChannel):
            if len(party_channel.members) == 0:
                # We probably just left, so don't do anything
                pass
            elif len(party_channel.members) == 1:
                if after.channel is None:
                    voice = member.guild.voice_client
                    await voice.disconnect(force=True)
                else:
                    await party_channel.connect()
            else:
                found_bot = False
                for each_user in party_channel.members:
                    if each_user.id == 1151658242108305539:
                        found_bot = True
                if not found_bot:
                    await party_channel.connect()
        if isinstance(sword_channel, discord.VoiceChannel):
            if len(sword_channel.members) == 0:
                # We probably just left, so don't do anything
                pass
            elif len(sword_channel.members) == 1:
                if after.channel is None:
                    voice = member.guild.voice_client
                    await voice.disconnect(force=True)
                else:
                    await sword_channel.connect()
            else:
                found_bot = False
                for each_user in sword_channel.members:
                    if each_user.id == 1151658242108305539:
                        found_bot = True
                if not found_bot:
                    await sword_channel.connect()


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(super_secret_token)
