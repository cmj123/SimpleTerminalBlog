from database import Database
from models.blog import Blog

__author__ = 'edijemeni'

class Menu(object):
    def __init__(self):
        self.user = raw_input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author':self.user})
        if blog is not None:
            self.user_blog = blog
            return True
        else:
            return False
    def _prompt_user_for_account(self):
        title = raw_input("Enter blog title: ")
        description = raw_input("Enter blog description: ")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write =  raw_input("Do you want to read (R) or write (W) blogs?")
        if read_or_write == 'R'
        # If read:
            # list blogs in database
            # allow user to pick one
            # display posts
            pass
        elif read_or_write == 'W':
            # checj if user has a blog
            # if they do, prompt to write a post
            # if not, prompt to create new blog
            pass
        else:
            print("Thank you for blogging!")

        pass

