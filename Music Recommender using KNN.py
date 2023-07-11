from sklearn.neighbors import NearestNeighbors

# Load and preprocess your music dataset

# Split the dataset into training and test sets

# Create the KNN model
knn_model = NearestNeighbors(n_neighbors=5, metric='euclidean')

# Fit the model on the training data
knn_model.fit(X_train)

# Perform recommendation for a specific song or user preferences
query_song = [0.5, 0.8, 0.2, ...]  # Features of the song or user preferences
distances, indices = knn_model.kneighbors([query_song])

# Retrieve recommended songs based on the nearest neighbors
recommended_songs = [song_names[i] for i in indices.flatten()]

# Print the recommended songs
print("Recommended Songs:")
for song in recommended_songs:
    print(song)
