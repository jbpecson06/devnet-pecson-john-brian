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
    print("5. Remove a Movie")
    print("6. Exit")
    return input("Choose an option: ")


def add_movie(movie_list):
    added_movie = input("Enter Movie Title: ")
    added_director = input("Enter Director: ")
    movie_status = input("Status: ")

    movie = f"{added_movie} - {added_director} - {movie_status}"
    movie_list.append(movies)
    print("")
    print("Movie added successfully.")
    print("")


def view_movies(movie_list):    
    if not movie_list:
        print("")
        print("No movies in the collection")
        print("")
        return
 
    for number, movie in enumerate(movie_list, start=1):
        print(f"{number}. {movie}")


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


def remove_movie(movie_list):
    
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
            remove_movie(movies)
        elif choice == "6":
            print("Exit.")
            break
        else:
            print("Invalid!")


main()
