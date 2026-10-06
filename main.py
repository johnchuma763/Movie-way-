from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle


MOVIES = [
    ("The General", "1926", "Comedy / Adventure", "8.1"),
    ("Nosferatu", "1922", "Horror / Classic", "7.8"),
    ("The Kid", "1921", "Comedy / Drama", "8.2"),
    ("Metropolis", "1927", "Sci-Fi / Drama", "8.3"),
    ("The Lost World", "1925", "Adventure / Fantasy", "7.0"),
    ("The Great Train Robbery", "1903", "Western / Classic", "7.2"),
]


class MovieCard(BoxLayout):
    def __init__(self, movie, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.size_hint_y = None
        self.height = 150
        self.padding = 12
        self.spacing = 5

        with self.canvas.before:
            Color(0.055, 0.065, 0.08, 1)
            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[12]
            )

        self.bind(pos=self.update_bg, size=self.update_bg)

        title, year, genre, rating = movie

        self.add_widget(Label(
            text=title,
            font_size=22,
            bold=True,
            color=(0.1, 0.85, 0.45, 1)
        ))

        self.add_widget(Label(
            text=f"{year}  •  {genre}  •  ⭐ {rating}",
            font_size=14,
            color=(0.8, 0.8, 0.8, 1)
        ))

        watch = Button(
            text="WATCH",
            size_hint_y=None,
            height=42,
            background_normal="",
            background_color=(0.9, 0.12, 0.15, 1)
        )

        watch.bind(on_press=lambda x: self.watch_movie(title))
        self.add_widget(watch)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def watch_movie(self, title):
        print(f"Selected movie: {title}")


class MovieWayApp(App):

    def build(self):
        self.title = "MOVIEWAY"

        root = BoxLayout(
            orientation="vertical",
            padding=12,
            spacing=10
        )

        with root.canvas.before:
            Color(0.025, 0.03, 0.04, 1)
            self.background = RoundedRectangle(
                pos=root.pos,
                size=root.size
            )

        root.bind(
            pos=lambda obj, value: setattr(
                self.background, "pos", value
            ),
            size=lambda obj, value: setattr(
                self.background, "size", value
            )
        )

        title = Label(
            text="▶  MOVIEWAY",
            font_size=30,
            bold=True,
            size_hint_y=None,
            height=60,
            color=(0.1, 0.85, 0.45, 1)
        )

        root.add_widget(title)

        search = TextInput(
            hint_text="Search movies...",
            size_hint_y=None,
            height=48,
            multiline=False
        )

        root.add_widget(search)

        search_button = Button(
            text="SEARCH",
            size_hint_y=None,
            height=45,
            background_normal="",
            background_color=(0.15, 0.45, 0.95, 1)
        )

        root.add_widget(search_button)

        scroll = ScrollView()

        movie_list = BoxLayout(
            orientation="vertical",
            spacing=10,
            size_hint_y=None
        )

        movie_list.bind(
            minimum_height=movie_list.setter("height")
        )

        for movie in MOVIES:
            movie_list.add_widget(MovieCard(movie))

        scroll.add_widget(movie_list)
        root.add_widget(scroll)

        return root


if __name__ == "__main__":
    MovieWayApp().run()
