from elevenlabs import clone, generate, play
from elevenlabs import set_api_key
set_api_key("f75f72aeaa36eea5c5b85332abe98e4f")

voice = clone(
    name="Derek",
     description="An young American woman voice with a slight hoarseness in his throat. Perfect for news", # Optional
    # files=["./daniel01.mp3", "./daniel02.mp3", "./daniel03.mp3"],
    files=["./derek01.mp3", "./derek02.mp3", "./derek03.mp3"],
)

audio = generate(text="Is the concept baffling or is Aristotle balling? Are they mutually exclusive and if so can we ever truly know if his drip exists, sus, nigga?", voice=voice)

play(audio)