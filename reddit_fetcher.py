import praw

# Initialize Reddit API client
reddit = praw.Reddit(
    client_id="IsSCdsVa0IybF5_EjsGmGQ",
    client_secret="9sjK15W5jAB0jAQPxTqy7qWmsrPPDw",
    user_agent="myredditapp:v1.0 (by /u/sara__15)"
)

# Function to fetch posts from subreddit containing certain keywords
def fetch_posts(subreddit_name, keyword):
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.new(limit=50)  # Fetching new posts, limit to 10
    result = []

    # Loop through posts and check if the keyword is in the title or body
    for post in posts:
        print(post.title)
        if keyword.lower() in post.title.lower() or keyword.lower() in post.selftext.lower():
            result.append({
                'title': post.title,
                'url': post.url,
                'score': post.score,
                'comments': post.num_comments
            })

    return result

# Example usage
subreddit = "harrypotter"
keyword = "harry"
posts = fetch_posts(subreddit, keyword)

# Print the result
for post in posts:
    print(f"Title: {post['title']}")
    print(f"URL: {post['url']}")
    print(f"Score: {post['score']} | Comments: {post['comments']}")
    print("-" * 60)
    print(f"Connected to Reddit as: {reddit.user.me()}")

