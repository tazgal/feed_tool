
def feed_read_902_streamlit():
    url = "https://www.902.gr/feed/recent"
    feed = feedparser.parse(url)
    st.write("Title: ", feed.feed.title)
    for entry in feed.entries:
        st.write("Title:", entry.title)
        st.write("link", entry.link)
        if hasattr(entry,"published"):
            st.write("Published:", entry.published)
        st.write("----")

feed_read_902_streamlit()
