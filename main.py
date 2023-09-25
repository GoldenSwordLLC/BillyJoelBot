import discord
import pyaudio
from config import super_secret_token


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.party_connected = False
        self.sword_connected = False
        self.p = None
        self.SPEAKERS = None
        self.stream = None
        self.in_voice = False

    def setup_pyaudio(self):
        self.p = pyaudio.PyAudio()
        self.SPEAKERS = self.p.get_default_output_device_info()["index"]
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=2,
                                  rate=48000,
                                  input=True,
                                  frames_per_buffer=1024,
                                  # TODO - Is this actually a problem?
                                  input_device_index=self.SPEAKERS)

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
                    self.in_voice = True
                else:
                    voice = member.guild.voice_client
                    await voice.disconnect(force=True)
                    self.in_voice = False
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
                    self.in_voice = True
                else:
                    voice = member.guild.voice_client
                    await voice.disconnect(force=True)
                    self.in_voice = False

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
                    self.in_voice = False
                else:
                    if not self.in_voice:
                        await sword_channel.connect()
                        self.in_voice = True
            else:
                found_bot = False
                for each_user in party_channel.members:
                    if each_user.id == 1151658242108305539:
                        found_bot = True
                if not found_bot:
                    await party_channel.connect()
                    self.in_voice = True
        if isinstance(sword_channel, discord.VoiceChannel):
            if len(sword_channel.members) == 0:
                # We probably just left, so don't do anything
                pass
            elif len(sword_channel.members) == 1:
                if after.channel is None:
                    voice = member.guild.voice_client
                    await voice.disconnect(force=True)
                    self.in_voice = False
                else:
                    if not self.in_voice:
                        await sword_channel.connect()
                        self.in_voice = True
            else:
                found_bot = False
                for each_user in sword_channel.members:
                    if each_user.id == 1151658242108305539:
                        found_bot = True
                if not found_bot:
                    await sword_channel.connect()
                    self.in_voice = True

    async def play_music(self, member):
        while self.in_voice:
            if self.p is None and self.SPEAKERS is None and self.stream is None:
                self.setup_pyaudio()
            music_data = self.stream.read(1024, exception_on_overflow=False)
            voice = member.guild.voice_client
            # TODO - Figure out the encode param here
            voice.send_audio_packet(music_data, encode=the_music.is_opus())
        self.stream.close()
        self.p.terminate()
        self.p = None
        self.SPEAKERS = None
        self.stream = None


intents = discord.Intents.default()

client = MyClient(intents=intents)
client.run(super_secret_token)
