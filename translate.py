from elevenlabs import clone, save, generate, play
from openai import OpenAI
from elevenlabs import set_api_key
from api_keys import ELEVEN_LABS_API_KEY,  OPENAI_API_KEY

set_api_key(ELEVEN_LABS_API_KEY)


da1 = "怎  么 能   哭 呢 一 切  会  好  哒 一 切  都  去 吧 你 就  得  想  着"
bingchiling = "早上好中国 现在我有冰淇淋 我很喜欢冰淇淋 但是 速度与激情9 比冰淇淋 速度与激情 速度与激情9 我最喜欢 所以…现在是音乐时间 准备 1 2 3 两个礼拜以后 速度与激情9 ×3 不要忘记 不要错过 记得去电影院看速度与激情9 因为非常好电影 动作非常好 差不多一样冰淇淋 再见"
redsun = "天上太阳红呀红彤彤诶心中的太阳是毛泽东诶他领导我们得解放诶人民翻身当家做主人咿呀咿吱呦喂呀而呀吱呦啊人民翻身当家做主人"
client = OpenAI(api_key=OPENAI_API_KEY)

audio_file = open("derektest5.mp3", "rb")
transcript = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
  )

print(transcript)


def VoiceClone(text):
  voice = clone(
      name="Derek",
      description="Asian-American Male, age 17, english accent", # Optional
      files=["./derek01.mp3", "./derek02.mp3", "./derek03.mp3"],
  )

  audio = generate(text=f"{text}", voice=voice)
  save(audio, f"derek.mp3")
  play(audio)
  print(type(audio))


def process(text):
  VoiceClone(text)


process(transcript)