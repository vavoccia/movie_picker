import media
import fresh_tomatoes




toy_story = media.Movie("Toy Story", "A story about a boy and his toys that come to life", 
                        "https://upload.wikimedia.org/wikipedia/fi/thumb/e/ee/Toy_Story_Juliste.jpg/250px-Toy_Story_Juliste.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",3.5)
avatar = media.Movie("Avatar", "A marine on a alien planent", 
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY",3)
avatar2 = media.Movie("Avatar", "A marine on a alien planent", 
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY",2.5)
avatar3 = media.Movie("Avatar", "A marine on a alien planent", 
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY",1.5)
avatar4 = media.Movie("Avatar", "A marine on a alien planent", 
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY",4)
avatar5 = media.Movie("Avatar", "A marine on a alien planent", 
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY",2)
avatar6 = media.Movie("Avatar", "A marine on a alien planent", 
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY",1.5)
avatar7 = media.Movie("Avatar", "A marine on a alien planent", 
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY",4)
avatar8 = media.Movie("Avatar", "A marine on a alien planent", 
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY",2)
movies = [toy_story, avatar, avatar2, avatar3, avatar4, avatar5, avatar6, avatar7, avatar8]
fresh_tomatoes.open_movies_page(movies)
