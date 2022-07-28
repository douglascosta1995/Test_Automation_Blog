from blog import Blog
MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post,"q" to quit'
POST_TEMPLATE = '''
    -----{}-----
    
    {}
    '''
blogs = dict() # blog_name : Blog object


def menu():
    print_blogs()
    selection = input(MENU_PROMPT)

    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))


def ask_create_blog():
    blog_title = input('What is the blog name? ')
    author_name = input('What is your name? ')
    blogs[blog_title] = Blog(blog_title, author_name)


def ask_read_blog():
    blog_title = input('Enter the blog title: ')

    print_posts(blogs[blog_title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_name = input('Which blog do you want to write your post in?' )
    title = input('What is the title of the post?')
    content = input('What is the content of the post? ')

    blogs[blog_name].create_post(title, content)