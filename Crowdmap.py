class Crowdmap(object):
    def __init__(self, init_list):
      self.list = init_list
      
    def get_all_posts_for(self, name):
        return [post for post in self.list if post.find(name) != -1]

    def is_location_for_name(self, name):
		posts = [post for post in self.list if post.find(name) != -1 and post.find("at") != -1]
		return len(posts) != 0

    def if_there_are_map_inconsistencies(self, name):
		posts = [post for post in self.list if post.find(name) != -1 and post.find("at") != -1]
		x=posts[0].index("at")
		posts1 = [post for post in self.list if post.find(name) != -1 and  post.find(posts[0][x:x+4]) != -1]
		print '\n'+posts[0][x:x+4]
		return len(posts) != len(posts1)
		
    def if_there_are_map_inconsistencies_allnameplace(self, name):
		posts = [post for post in self.list if post.find(name) != -1 and post.find("at") != -1]
		words=posts[0].split()
		place=words.index('at')+1
		posts1 = [post for post in self.list if post.find(name) != -1 and  post.find(posts[0][place]) != -1]
		print '\n'+posts[0][place]
		return len(posts) != len(posts1)
		
