from googletrans import Translator


t = Translator()
print(t.translate('Hallo Welt', 'ja').text)


