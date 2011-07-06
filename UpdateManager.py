import urllib, simplejson, subprocess, os

class GithubUpdateManager():
	"""An update-manager using github commits"""
	github_base_url = "https://api.github.com/repos/"
	
	def __init__(self,user,repository,branch="master"):
		"""docstring for __init__"""
		self.user = user
		self.repository = repository
		self.branch = branch
	#end def __init__
	
	def check(self):
		"""docstring for check"""
		url = self.github_base_url+self.user+"/"+self.repository+"/git/refs/heads/"+self.branch
		ref_info = urllib.urlopen(url)
		result = simplejson.load(ref_info)
		remote_sha = result['object']['sha']
		
		pr = subprocess.Popen(['/usr/bin/git','rev-parse','HEAD'],
							cwd=os.path.abspath(''),
							stdout=subprocess.PIPE,
							stderr=subprocess.PIPE,
							shell=False)
		(out,error) = pr.communicate()
		local_sha = out.strip()
		return (local_sha == remote_sha)
	#end def check
	
	def update(self):
		"""docstring for update"""
		pr = subprocess.Popen(['/usr/bin/git','pull','origin'],
							cwd=os.path.abspath(''),
							stdout=subprocess.PIPE,
							stderr=subprocess.PIPE,
							shell=False)
		(out,error) = pr.communicate()
		print out
	#end def update
	
if(__name__ == "__main__"):
	gum = GithubUpdateManager("Chaosbit","headphones","working")
	print gum.check()
	gum.update()