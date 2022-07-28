blogs = dict() # blog_name : Blog object

def menu():
    # Show the user the available blogs
    # Let the user make a choice
    # Do sth with that choice
    #Eventually exit

    print_blogs()

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))
        