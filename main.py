import discord
from discord import ClientException

from config import super_secret_token

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}.')
        party_channel_id = 1151092359048724544
        party_channel = client.get_channel(party_channel_id)
        if isinstance(party_channel, discord.VoiceChannel):
            if len(party_channel.members) == 0:
                pass
            if len(party_channel.members) >= 1:
                found_bot = False
                for each_user in party_channel.members:
                    if each_user.id == 1151658242108305539:
                        found_bot = True
                if not found_bot:
                    await party_channel.connect()

    async def on_voice_state_update(self, member, before, after):
        found_bot = False
        party_channel_id = 1151092359048724544
        #sword_channel_id = 1151755897366904914
        party_channel = client.get_channel(party_channel_id)
        #sword_channel = client.get_channel(sword_channel_id)
        if isinstance(party_channel, discord.VoiceChannel):
            print(f'How many members: {len(party_channel.members)}')
            if len(party_channel.members) == 0:
                print(f'Len in 0: {len(party_channel.members)}')
                # We probably just left, so don't do anything
                pass
            if len(party_channel.members) == 1:
                print(f'Len in == 1: {len(party_channel.members)}')
                if member.id == 1151658242108305539:
                    voice = member.guild.voice_client
                    await voice.disconnect(force=True)
                else:
                    for each_user in party_channel.members:
                        if each_user.id == 1151658242108305539:
                            found_bot = True
                    if not found_bot:
                        await party_channel.connect()
            else:
                print(f'Len in else: {len(party_channel.members)}')
                found_bot = False
                for each_user in party_channel.members:
                    if each_user.id == 1151658242108305539:
                        found_bot = True
                if not found_bot:
                    await party_channel.connect()
        #elif isinstance(sword_channel, discord.VoiceChannel):
        #    if len(sword_channel.members) == 1:
        #        print(str(member))
        #        if member.id == 1151658242108305539:
        #            voice = member.guild.voice_client
        #            await voice.disconnect(force=False)
        #    else:
        #        await sword_channel.connect()


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(super_secret_token)
