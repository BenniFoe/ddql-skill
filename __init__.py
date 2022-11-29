from mycroft import MycroftSkill, intent_file_handler


class Ddql(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ddql.intent')
    def handle_ddql(self, message):
        self.speak_dialog('ddql')


def create_skill():
    return Ddql()

