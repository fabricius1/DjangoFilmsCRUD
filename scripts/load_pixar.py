from films.models import Film, Genre
import csv


def run():
    with open('films/pixar.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Film.objects.all().delete()
        Genre.objects.all().delete()

        for row in reader:
            print(row)

            genre, _ = Genre.objects.get_or_create(name=row[-1])

            film = Film(title=row[0],
                        length=row[1],
                        year=row[2],
                        genre=genre)
            film.save()