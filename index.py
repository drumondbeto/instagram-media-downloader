import instaloader

def download_post_from_url(url_post):
    if (url_post != ""):
        if(url_post[- 1] != "/"):
            url_post = url_post + "/"
        
        shortcode = url_post.split("/")[-2]
        download_post_from_code(shortcode)


def download_post_from_code(shortcode):
    if (shortcode != ""):
        L = instaloader.Instaloader()
        folderName = "downloads"
        L.download_post(instaloader.Post.from_shortcode(L.context, shortcode), target=folderName)

# Use exemples:
# download_post_from_url("https://www.instagram.com/p/DIe7hWwSOTv/")
# download_post_from_code("DIe7hWwSOTv")
