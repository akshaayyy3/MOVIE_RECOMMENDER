import streamlit as st
from src.hybrid import hybrid_recommend
from src.tmdb import fetch_tmdb_details

# 🌟 Streamlit Page Config
st.set_page_config(page_title="🎬 Hybrid Movie Recommender", layout="wide")
st.title("🎥 Hybrid Movie Recommendation System")
st.markdown("#### Discover movies tailored *just for you!* 🍿")

# 🎯 User Input
user_id = st.number_input("Enter User ID:", min_value=1, max_value=60000, value=1, step=1)

# 🔘 Button
if st.button("🎬 Get Recommendations"):
    with st.spinner("🔍 Finding the best movies for you..."):
        recs = hybrid_recommend(user_id=user_id)

    if recs is None or recs.empty:
        st.error("No recommendations found for this user. Try a different User ID!")
    else:
        st.success(f"✅ Found {len(recs)} recommendations!")

        # 🖼️ Display recommendations in grid (3 per row)
        num_cols = 3
        rows = (len(recs) // num_cols) + 1

        for i in range(rows):
            cols = st.columns(num_cols)
            for j in range(num_cols):
                idx = i * num_cols + j
                if idx < len(recs):
                    movie = recs.iloc[idx]
                    poster, overview = fetch_tmdb_details(movie["movieId"])

                    with cols[j]:
                        st.markdown(f"### 🎞️ {movie['title']}")
                        if poster:
                            st.image(poster, use_container_width=True)
                        else:
                            st.image("https://via.placeholder.com/300x450?text=No+Poster", use_container_width=True)

                        st.caption(f"⭐ Hybrid Score: {round(movie['hybrid_score'], 2)}")
                        with st.expander("📖 Overview"):
                            st.write(overview or "No description available.")
