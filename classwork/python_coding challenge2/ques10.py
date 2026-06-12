# Ratings given by users for movies:
# ratings = { 
#     "Inception": 4.8, 
#     "Avatar": 4.3, 
#     "Titanic": 4.5, 
#     "Joker": 4.7, 
#     "Frozen": 3.8, 
#     "Interstellar": 4.9, 
#     "Dune": 4.6, 
#     "Up": 4.1, 
#     "Coco": 4.4, 
#     "Cars": 3.9 
# } 
# Tasks 
# 1. Display movies rated above 4.5.  
# 2. Find the highest-rated movie.  
# 3. Find the lowest-rated movie.  
# 4. Calculate average rating.  
# 5. Create a recommendation list (rating ≥ 4.5).

ratings = { 
    "Inception": 4.8, 
    "Avatar": 4.3, 
    "Titanic": 4.5, 
    "Joker": 4.7, 
    "Frozen": 3.8, 
    "Interstellar": 4.9, 
    "Dune": 4.6, 
    "Up": 4.1, 
    "Coco": 4.4, 
    "Cars": 3.9 
}

# --- Task 1: Display movies rated above 4.5 ---
print("--- Movies rated above 4.5 ---")
ratings_items = list(ratings.items())
for item in ratings_items:
    if item[1] > 4.5:
        print(item[0], ":", item[1])
print("\n" + "-" * 40)

# --- Task 2: Find the highest-rated movie ---
print("--- Highest-Rated Movie ---")
highest_movie = ratings_items[0][0]
highest_rating = ratings_items[0][1]
for item in ratings_items:
    if item[1] > highest_rating:
        highest_movie = item[0]
        highest_rating = item[1]
print("Highest-Rated Movie:", highest_movie, "with a rating of", highest_rating)
print("\n" + "-" * 40)

# --- Task 3: Find the lowest-rated movie ---
print("--- Lowest-Rated Movie ---")
lowest_movie = ratings_items[0][0]
lowest_rating = ratings_items[0][1]
for item in ratings_items:
    if item[1] < lowest_rating:
        lowest_movie = item[0]
        lowest_rating = item[1]
print("Lowest-Rated Movie:", lowest_movie, "with a rating of", lowest_rating)
print("\n" + "-" * 40)

# --- Task 4: Calculate average rating ---
print("--- Average Rating ---")
total_rating = 0
for item in ratings_items:
    total_rating += item[1]
average_rating = total_rating / len(ratings_items)
print(f"Average movie rating: {average_rating:.2f}")
print("\n" + "-" * 40)

# --- Task 5: Create a recommendation list (rating ≥ 4.5) ---
print("--- Recommendation List ---")
recommendation_list = []
for item in ratings_items:
    if item[1] >= 4.5:
        recommendation_list.append(item[0])
print("Recommended Movies (Rating ≥ 4.5):", recommendation_list)
print("\n" + "-" * 40)