from pyramid.i18n import TranslationStringFactory
_ = TranslationStringFactory('kotti_theme_superhero')


def kotti_configure(settings):

    settings['kotti.fanstatic.view_needed'] = 'kotti_theme_superhero.static.view_needed'
    settings['kotti.fanstatic.edit_needed'] = 'kotti_theme_superhero.static.edit_needed'
