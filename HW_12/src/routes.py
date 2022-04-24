from HW_12.src.template_renders import template_renders


def setup_routes(app):
    app.router.add_route('GET', '/', template_renders.index, name='index')
    app.router.add_route('GET', '/some_ftb/', template_renders.all_ftb_matches, name='all_ftb_matches')
    app.router.add_route('GET', '/itl_ftb/', template_renders.all_itl_matches, name='all_itl_matches')
    app.router.add_route('GET', '/nhl_res/', template_renders.all_nhl_matches, name='all_nhl_matches')
    app.router.add_static('/css', 'src/static/css')
    app.router.add_static('/some_ftb/css', 'src/static/css')
    app.router.add_static('/itl_ftb/css', 'src/static/css')
    app.router.add_static('/nhl_res/css', 'src/static/css')
    