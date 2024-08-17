<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Movie Recommender System</h1>

<h2>Overview</h2>
<p>This project is a movie recommender system built using Python. The system utilizes a content-based filtering approach to suggest movies similar to a given input. It processes metadata such as the movie overview, genres, keywords, cast, and crew to generate a set of tags for each movie. The similarity between movies is computed using cosine similarity, allowing for efficient and relevant recommendations.</p>

<h2>Features</h2>
<ul>
    <li><strong>Content-Based Filtering:</strong> Uses metadata (e.g., genres, keywords, cast) to recommend similar movies.</li>
    <li><strong>Cosine Similarity:</strong> Measures the similarity between movies based on tags.</li>
    <li><strong>Top 5 Recommendations:</strong> For any given movie, the system returns the top 5 similar movies.</li>
    <li><strong>Pickle for Serialization:</strong> Movie data and similarity matrices are serialized using <code>pickle</code> for easy reuse.</li>
</ul>

<h2>Project Structure</h2>
<ul>
    <li><strong>Data Preparation:</strong> Combines movie metadata (overview, genres, keywords, cast, and crew) to create a "tags" column.</li>
    <li><strong>Vectorization:</strong> Converts the tags into numerical form using a vectorizer to prepare them for similarity comparison.</li>
    <li><strong>Similarity Computation:</strong> Uses cosine similarity to compute pairwise similarity scores between movies.</li>
    <li><strong>Recommendation Function:</strong> A function that takes a movie title as input and returns the top 5 most similar movies.</li>
</ul>

<h2>How to Use</h2>
<ol>
    <li><strong>Setup:</strong>
        <ul>
            <li>Ensure you have Python installed along with the required libraries.</li>
            <li>You can install necessary libraries using:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
        </ul>
    </li>
    <li><strong>Run the Recommender:</strong>
        <ul>
            <li>Load the notebook or run the Python script to use the recommender system.</li>
            <li>Use the <code>recommend()</code> function to get movie recommendations.
                <pre><code>recommend('Avatar')</code></pre>
            </li>
            <li>The system will output a list of movies similar to "Avatar."</li>
        </ul>
    </li>
</ol>

<h2>Example</h2>
<p>For the movie "Avatar," the system recommends:</p>
<ul>
    <li>Aliens vs Predator: Requiem</li>
    <li>Aliens</li>
    <li>Falcon Rising</li>
    <li>Independence Day</li>
    <li>Titan A.E.</li>
</ul>

<h2>Files</h2>
<ul>
    <li><strong>movie-reccomender.ipynb:</strong> The Jupyter Notebook containing the entire codebase.</li>
    <li><strong>movie_dict.pkl:</strong> Serialized dictionary of movie data.</li>
    <li><strong>similarity.pkl:</strong> Serialized cosine similarity matrix.</li>
</ul>

<h2>Dependencies</h2>
<ul>
    <li>Python 3.x</li>
    <li>Required Python libraries:
        <ul>
            <li>pandas</li>
            <li>numpy</li>
            <li>sklearn</li>
            <li>pickle</li>
        </ul>
    </li>
</ul>

<h2>Future Enhancements</h2>
<ul>
    <li>Add user-based collaborative filtering for personalized recommendations.</li>
    <li>Implement a web interface using Streamlit for easy interaction.</li>
    <li>Expand the dataset to include more features like user ratings.</li>
</ul>

<h2>Contact</h2>
<p>For any queries or contributions, please reach out to the repository maintainer.</p>

</body>
</html>
