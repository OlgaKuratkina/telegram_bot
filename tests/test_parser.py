from source_parser.parser import parse


quote1 = "#414563 [15823 votes]\n05.12.2011 в  9:12\nKotyara: Российские смесители - от обморожения до ожога один шаг!"
quote2 = """#438212 [8275 votes]
02.03.2016 в  9:44
Как-то давно знакомый позвонил и говорит - год назад ты собирал мне комп, не мог бы заменить сдром на более удобный?
- не читает сд?
- читает.
- не читает двд?
- читает.
- не пишет?
- всё пишет.
- хм, а что не так-то?
- неудобный.

Привёз он комп, оказалось - сдром кверху ногами установлен. (собирал-то боком системный блок, на столе)
Перевернул - и человек снова доволен - теперь диск не надо придерживать когда вставляешь. Да и не падает, когда выезжает."""


def test_parse():
    with open('data/random_page.html') as f:
        assert parse(f) == quote1


def test_parse_multiple_lines():
    with open('data/random_page2.html') as f:
        assert parse(f) == quote2

