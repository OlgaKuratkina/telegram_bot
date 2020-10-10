from source_parser.parser import parse


def test_parse():
    with open('data/random_page.html') as f:
        assert parse(f) == 'Kotyara: Российские смесители - от обморожения до ожога один шаг!'


def test_parse_multiple_lines():
    with open('data/random_page2.html') as f:
        assert parse(f) == """Как-то давно знакомый позвонил и говорит - год назад ты собирал мне комп, не мог бы заменить сдром на более удобный?
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

