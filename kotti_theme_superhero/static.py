from fanstatic import Library
from fanstatic import Resource
from kotti.fanstatic import NeededGroup
from kotti.fanstatic import edit_needed_js
from kotti.fanstatic import view_needed_js


library = Library(
    "kotti_theme_superhero",
    "static")
superhero_css = Resource(
    library,
    "bootstrap.css",
    minified="bootstrap.min.css")

edit_needed = NeededGroup([
    superhero_css,
    edit_needed_js,
    ])
view_needed = NeededGroup([
    superhero_css,
    view_needed_js,
    ])
