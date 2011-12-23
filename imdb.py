from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
class Actor:
    def __init__(self,id):
        print id
        self.page = BeautifulSoup(urlopen("http://www.imdb.com/name/"+id+"/filmoyear"))       
        self.name = self.page.title.text[:-22]       
        self.id =  id
        self.filmography = set()
        self.getFilmography()
    def getFilmography(self):
        print "Getting filmography of "+self.name
        for i in self.page.findAll("div",{"id":"tn15content"}):
            for j in i.findAll("li"):
                self.filmography.add(im.films.at(j.a['href'].split("/")[2]))

class Film:
    def __init__(self,id):
        page = BeautifulSoup(urlopen("http://www.imdb.com/title/"+id+"/fullcredits"))
        self.title = page.find("div",{"id":"tn15title"}).a.text
        self.id = id
        self.cast = set()
        print "Getting cast of "+self.title
        for i in page.findAll("td",{"class":"nm"}):
            im.actors.at(i.a['href'].split("/")[2])
            
    def hasActor(self,id):
        for i in self.cast:
            if i.id == id:
                return True
        return False
            
class Films:
    def __init__(self):
        # Mapping from id to film object
        self.films = dict()
        
    def at(self,id):
        print "Looking up film "+id
        try:
            return self.films[id]
        except KeyError:
            fi = Film(id)
            self.films[id] = fi
            return fi
    
class Actors:
    def __init__(self):
        # Mapping from id to actor object
        self.actors = dict()
        self.marked = False
        
    def at(self,id):
        print "Looking up actor "+id
        try:
            return self.actors[id]
        except KeyError:
            ac = Actor(id)
            self.actors[id] = ac
            return ac
   
class IMDB:
    def __init__(self):
        self.prefix = ""
        self.films = Films()
        self.actors = Actors()
    def addActor(self,id):
        self.actors.at(Actor(id))

    def separation(self,a1,a2):
        count = 0
        q = list()
        q.append(self.actors.at(a1))
        q[0].marked = True
        while len(q) > 0:
            t = q.pop()
            for i in t.filmography:
                if i.hasActor(a2):
                    return count
                for j in i.cast.filmography:
                    if not j.marked:
                        j.marked = True
                        q.insert(0,j)
            count += 1
        return "No connection"
        

im = IMDB()
im.addActor("nm0000288")

print im.separation("nm0000288","nm0004266")
    
##for i in im.actors:
##    print i.name+" films are:"
##    for j in i.filmography:
##        print "\t"+f.title(j)
