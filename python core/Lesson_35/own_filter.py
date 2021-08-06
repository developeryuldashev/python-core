from telegram.ext import MessageFilter
class HandlePython(MessageFilter):
    name='Filters.python'

    def filter(self, message):
        return 'python' in message

python=HandlePython()

class FilterAwesome(MessageFilter):
    def filter(self, message):
        return 'Dilshod' in message.text
filter_awesome=FilterAwesome()

class FilterRaxmat(MessageFilter):
    def raxmat(self,message):
        return 'raxmat' in message.text
filter_raxmat=FilterRaxmat()