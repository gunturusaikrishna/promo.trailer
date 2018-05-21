#!/usr/bin/env python
import media
import fresh_tomatoes

rgrm = media.Movie("Race Gurram", "action", "https://bit.ly/2x0Oa2q",
                   "https://www.youtube.com/embed/nda6eGtu8DI")
mstr = media.Movie("Mister", "love story", "https://bit.ly/2rXN2Xz",
                   "https://www.youtube.com/embed/b6TQ4tWGiPI")
kp = media.Movie("KUNGFU PANDA3", "Cartoon", "https://bit.ly/2rWPNJD",
                 "https://www.youtube.com/embed/10r9ozshGVE")
incd = media.Movie("INCREDIBLES", "CARTOON", "https://bit.ly/2rYfr0o",
                   "https://www.youtube.com/embed/i5qOzqD9Rms")
stnd = media.Movie("spy the next door", "detective", "https://bit.ly/2ICRc2s",
                   "https://www.youtube.com/embed/fa2RZf0m39g")
fiza = media.Movie("fiza", "love story", "https://bit.ly/2IUmzol",
                   "https://www.youtube.com/embed/2DEJTRwuEi4")
movies = [rgrm, mstr, kp, incd, stnd, fiza]
fresh_tomatoes.open_movies_page(movies)
