# Name: Jose Marrero
# Z number: Z23816617

# Step A
import csv 
def read_top_rated(filename: str) -> dict:
    """read top-rated movies into a dictionary keyed by title and year."""
    movies = {}

    with open(filename, "r", newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)

        for row in csv_reader:
            title = row[1]
            year = row[2]
            movies[(title, year)] = True

    return movies

def display_top_collaborations(limit: int | None = None) -> None:
    movies = read_top_rated("imdb-top-rated.csv")
    counts = {}

    with open("imdb-top-casts.csv", "r", newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            title = row[0]
            year = row[1]
            director = row[2]
            actors = row[3:]
            if (title, year) in movies:
                for actor in actors:
                    actor = actor.strip()
                    if actor:
                        cast_pair = (director, actor)
                        if cast_pair not in counts:
                            counts[cast_pair] = 1
                        else:
                            counts[cast_pair] += 1


    rankings_sorted = []

    for cast_pair, count in counts.items():
        director, actor = cast_pair
        rankings_sorted.append((count, director, actor))

    rankings_sorted.sort(reverse=True)

    for count, director, actor in rankings_sorted[:limit]:
        print((director, actor, count))

# Step B

def read_top_grossing(filename: str) -> dict:
    rated_movies = {}
    with open(filename, "r", newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)

        for row in csv_reader:
            title = row[1]
            year = row[2]
            earnings = float(row[3])
            rated_movies[(title, year)] = earnings

    return rated_movies

def display_top_actors(limit: int | None = None) -> None:
    grosing_movie = read_top_grossing( "imdb-top-grossing.csv") 
    actor_total = {}

    with open("imdb-top-casts.csv", "r", newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            title = row[0]
            year = row[1]
            actors = row[3:]

            if (title, year) in grosing_movie:
                total_earnings = grosing_movie[(title, year)]
                for actor in actors:
                    actor = actor.strip()
                    if actor:
                        if actor not in actor_total:
                            actor_total[actor] = total_earnings
                        else: 
                            actor_total[actor] += total_earnings

    sorted_ranks = []
    for actor, total in actor_total.items():
        sorted_ranks.append((total, actor))

    sorted_ranks.sort(reverse=True)
    for total, actor, in sorted_ranks[:limit]:
        print((actor, total))
# Step C

def main() -> None:
    """This displays the top 10 entries in both type of movie rankings"""
    print("Top 10 director and –actor pairs:")
    display_top_collaborations(10)

    print("\nTop 10 actors by box office:")
    display_top_actors(10)

    print("Name: Jose Marrero Znumber = Z23816617")

main()