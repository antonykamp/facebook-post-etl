import argparse
import time
from facebook_scraper import *
import os

start_url = None


def handle_pagination_url(url):
    global start_url
    start_url = url


def extract_posts(
    username: str,
    min_num_posts: int,
    filename: str,
    cookie_location: str,
):
    """
    Extracts posts from a Facebook user's profile and saves them to a file.
    :param username: Facebook username
    :param min_num_posts: Minimum number of posts to scrape
    :param filename: Filename to save scraped posts
    :param cookie_location: Location of cookies.json
    :return: List of posts
    """
    print("--- Extracting posts ---")
    results = []
    while len(results) <= min_num_posts:
        try:
            for post in get_posts(
                username,
                cookies=cookie_location,
                page_limit=None,
                start_url=start_url,
                request_url_callback=handle_pagination_url,
                posts_per_page=200,
            ):
                results.append(post)
            print(f"Scraped {len(results)} posts")
            with open(filename, "w") as f:
                json.dump({"data": results}, f, default=str)
        except exceptions.TemporarilyBanned as e:
            print("Temporarily banned, sleeping for 10m")
            time.sleep(600)
    return results


def load_or_extract_posts(filename: str, **kwargs):
    """
    Loads posts from a file if it exists, otherwise extracts them from Facebook.
    :param filename: Filename to save scraped posts
    :return: List of posts
    """
    if os.path.exists(filename):
        print("--- Loading posts from file ---")
        with open(filename, "r") as f:
            data = json.load(f)
            results = data["data"]
            return results
    else:
        return extract_posts(filename=filename, **kwargs)


def filter_posts(posts: any, search_token: list[str]):
    """
    Filters posts by a search token.
    :param posts: List of posts
    :param search_token: List of search token to filter posts
    :return: Filtered list of posts
    """
    print("--- Filtering posts ---")

    if search_token is None:
        return posts
    return [
        post
        for post in posts
        if post["text"] is not None
        and any(word.lower() in post["text"].lower() for word in search_token)
    ]


def build_post_filename(post: any):
    """
    Builds a filename for a post.
    :param post: Post
    :return: Filename with timestamp and post ID
    """
    return f"{str(post['timestamp'])}-{str(post['post_id'])}.txt"


def build_post_file_content(post: any):
    """
    Builds the content of a post file.
    :param post: Post
    :return: Content of post file with text, URL, and time
    """
    return f"{post['text']}\n\nURL: {post['post_url']}\n\nTime: {post['time']}"


def save_as_txt(posts: any, folder: str):
    print("--- Saving posts ---")
    if not os.path.exists(folder):
        os.makedirs(folder)
    for post in posts:
        file = os.path.join(folder, build_post_filename(post))
        with open(file, "w") as f:
            f.write(build_post_file_content(post))


def execute(
    scraped_posts_filename: str,
    search_token: list[str],
    filtered_posts_folder: str,
    **kwargs,
):
    posts = load_or_extract_posts(filename=scraped_posts_filename, **kwargs)
    filtered_posts = filter_posts(posts, search_token)
    save_as_txt(filtered_posts, filtered_posts_folder)


def execute_on_args():
    parser = argparse.ArgumentParser(description="Facebook Post ETL")

    parser.add_argument(
        "--scraped_posts",
        type=str,
        default="scraped.json",
        help="Filename to save scraped posts",
    )
    parser.add_argument("--username", type=str, help="Facebook username")
    parser.add_argument(
        "--min_num_posts",
        type=int,
        help="Minimum number of posts to scrape",
    )
    parser.add_argument(
        "--filtered_posts",
        type=str,
        default="posts2",
        help="Folder to save filtered posts",
    )
    parser.add_argument(
        "--search_token", type=str, nargs="*", help="Search token to filter posts"
    )
    parser.add_argument("--cookies", type=str, help="Location of cookies.json")

    args = parser.parse_args()
    print(args)
    execute(
        scraped_posts_filename=args.scraped_posts,
        filtered_posts_folder=args.filtered_posts,
        search_token=args.search_token,
        cookie_location=args.cookies,
        username=args.username,
        min_num_posts=args.min_num_posts,
    )


if __name__ == "__main__":
    execute_on_args()
