def translate_day(day):
    """
    Translate day name from English to Hebrew
    :param day: day in English
    :return: day in Hebrew (with English letters)
    """
    translations = {
        "sunday": "Yom Rishon",
        "monday": "Yom Shenee",
        "tuesday": "Yom Shlishee",
        "wednesday": "Yom Revi'ee",
        "thursday": "Yom Chameeshee",
        "friday": "Yom Sheeshee",
        "saturday": "Yom Shabat",
    }
    return translations[day]


def part1_get_friday_day():
    return translate_day("friday")


def main():
    print(part1_get_friday_day())

main()