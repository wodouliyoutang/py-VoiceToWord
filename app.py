import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.say('新时代以来的十年，在党和国家发展进程中极不寻常、极不平凡。面对影响党长期执政、国家长治久安、人民幸福安康的突出矛盾和问题，以习近平同志为核心的党中央团结带领全党全军全国各族人民义无反顾进行具有许多新的历史特点的伟大斗争，创造了新时代的伟大成就，推动我国迈上全面建设社会主义现代化国家新征程。')
# engine.say('下面是英文 ')
engine.say('   how are you')
voices = engine.getProperty('voices')  

engine.runAndWait()
engine.stop()
