import random


def random_string():
    random_list = [
        "Пожалуйста, попробуйте написать что-нибудь более описательное.",
        "Ой! Кажется, ты написал что-то, чего я пока не понимаю",
        "Вы не против попробовать перефразировать это?",
        "Мне очень жаль, я не совсем уловил это.",
        "Я пока не могу ответить на этот вопрос, попробуйте спросить что-нибудь еще."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
