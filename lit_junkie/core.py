from lit_junkie.views import ALL_VIEWS, Quit


def main():
    start = ALL_VIEWS[0]  # Gets the first view.
    next_route = start.display()

    while True:
        for view in ALL_VIEWS:
            if next_route.name == view.name:
                next_route = view.display()
                break
        if next_route is None:
            break


def run():
    try:
        main()
    except KeyboardInterrupt:
        Quit().display()
