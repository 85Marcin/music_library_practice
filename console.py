from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository

artist1 = Artist("John Coltrane")
artist2 = Artist("Miles Davies")

artist_repository.save(artist1)
artist_repository.save(artist2)

artists = artist_repository.select_all()

