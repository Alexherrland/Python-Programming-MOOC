# Write your solution here:
class Series:
    def __init__(self, title, seasons, genres):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def __str__(self):
        genre_string = ", ".join(self.genres)
        if self.ratings:
            avg_rating = round(sum(self.ratings) / len(self.ratings), 1)
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{len(self.ratings)} ratings, average {avg_rating} points"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\nno ratings"
    
    def rate(self, rating):
        if 0 <= rating <= 5:
            self.ratings.append(rating)


def minimum_grade(rating, series_list):
    return [series for series in series_list if series.ratings and sum(series.ratings) / len(series.ratings) >= rating]


def includes_genre(genre, series_list):
    return [series for series in series_list if genre in series.genres]