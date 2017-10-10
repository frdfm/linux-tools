from nltk.chat.util import Chat, reflections

pairs = [["My name is (.*)",['Hi %1',]],['Hi',['Hi']],]

def bot():
	print "Type something!"
	chat = Chat(pairs, reflections)
	chat.converse()


bot()


