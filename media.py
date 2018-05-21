#!/usr/bin/env python
import webbrowser


class Movie():
    '''
    class Movie():
    Here class name is taken as Movie and set of attributes
    declared inside the movie class.

    Attributes:
    attr1 (promoTitle): Title of promo
    attr2 (promoStoryLine): Storyline of promo
    attr3 (promoImage): Image of promo
    attr4 (promoTrailer): Access youtube url
    '''

    validRATINGS = ["*****", "****", "***", "**", "*"]

    def __init__(self, promoTitle,
                 promoStoryLine, promoImage, promoTrailer):
        self.title = promoTitle
        self.storyline = promoStoryLine
        self.poster_image_url = promoImage
        self.trailer_youtube_url = promoTrailer

    def show_trailer(self):

        '''
         As we imported webbrowser, we can open project in default browser.
        '''

        webbrowser.open(self.trailer_youtube_url)
