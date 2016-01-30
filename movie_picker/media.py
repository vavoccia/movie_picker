import webbrowser
class Movie(object):
    """description of class"""
    def __init__(self, _title, _storyline, _image, _trailer, _stars):
        self.title      = _title
        self.storyline  = _storyline
        self.poster_image_url      = _image
        self.trailer_youtube_url = _trailer
        self.stars = _stars
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

