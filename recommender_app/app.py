import pandas as pd
import streamlit as st

from recommendation import generate_recommendation


st.markdown('<style>body{background-image: url("https://i.redd.it/4fxxbm4opjd31.jpg"); \
background-repeat: no-repeat; background-attachment: fixed; background-size: 100% 100%;} \
body::before{content: ""; position: absolute; top: 0px; right: 0px; bottom: 0px; \
left: 0px; background-color: rgba(1,1,1,0.9);}</style>',unsafe_allow_html=True)

st.success('**::: Movie Recommendation Engine :::**')

st.markdown(
    """
<style>
[class^="st-b"]  {
    # color: white;
    font-family: monospace;
}
.css-1v4eu6x.e16nr0p30 {
    color: white;
}
.st-at {
    background-color: #000000;
}
.css-145kmo2{
    color: white;
}

.css-1l40rdr {
    padding: 0.5rem;
    font-size: 0.8rem;
    color: white;
    font-family: "IBM Plex Mono", monospace;
    text-align: right;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    line-height: 0.75;
}
.css-1vbb94r {
    color: white;
}

.css-1bebw7p {
    border-top: black;
    border-bottom: black;
    border: transparent;
    }

.css-1b32pqr {
    padding: 0.5rem;
    font-size: 1rem;
    text-align: center;
    background-color: rgb(240, 242, 246);
    color: rgb(128, 132, 149);
    }


</style>
""",
    unsafe_allow_html=True,
)


def main():
    input_s = st.empty()
    movie_name = st.text_input("Please enter a movie title", '')
    number_of_movie = st.slider('How many movies do you want?', 1, 30, 10)
    if movie_name:
        recommended_movies = generate_recommendation(movie_name, top=number_of_movie)
        if not recommended_movies:
            st.header(('Sorry, this movie is not present in the database!'))
        else:
            movie_df = pd.DataFrame({'Recommended Movies': recommended_movies})
            st.table(movie_df)
       
    
if __name__ == '__main__':
    main()
