from django.core.management.commands.makemessages import Command as Makemessages


class Command(Makemessages):
    """xgettext alias names in addition to standart _
    n: ngettext
    nl: ngettext_lazy
    p: pgettext
    pl: pgettext_lazy
    np: npgettext
    npl: npgettext_lazy
    _l: gettext_lazy
    _n: gettext_noop
    """
    xgettext_options = [
        *Makemessages.xgettext_options, *[
            '--keyword=n:1,2',
            '--keyword=nl:1,2',
            '--keyword=p:1c,2',
            '--keyword=pl:1c,2',
            '--keyword=np:1c,2,3',
            '--keyword=npl:1c,2,3',
            '--keyword=_l',
            '--keyword=_n',
        ]
    ]
