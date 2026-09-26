"""
Midterm Practical Exam — Movie Collection Manager
Student: John Brian O. Pecson
"""

movies = []


def display_menu():
    print("=== Movie Collection Manager ===")
    print("1. Add a Movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4. Find a movie")
    print("5. Exit")
    return input("Choose an option: ")


def add_movie(movie_list):
    added_movie = input("Enter Movie Title: ")
    added_director = input("Enter Director: ")
    movie_status = input("Status (Watched/Unwatched): ").strip().capitalize()

    movie = f"{added_movie} - {added_director} - {movie_status}"
    movie_list.append(movies)
    print("")
    print("Movie added successfully.")
    print("")


def view_movies(movie_list):    
    # loop through and print every movie
    # handle empty list
    pass


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


def main():
    while True:
        choice = display_menu()

        if choice == "1":
            add_movie(movies)
        elif choice == "2":
            view_movies(movies)
        elif choice == "3":
            count_watched_unwatched(movies)
        elif choice == "4":
            find_movie(movies)
        elif choice == "5":
            print("Exit.")
            break
        else:
            print("Invalid!")


main()
