class Esm_Famil:
    def __init__(self,word):
        self.num_of_players = 0
        self.word = word
        self.players = {}
        self.names = {}
        self.cities = {}
        self.foods = {}
        self.colors = {}

    def add_player(self,player_name):
        p=Player(player_name,self)
        self.players[player_name]=p
        self.num_of_players+=1

    def calculate_scores(self,obj_dic):
        for o in obj_dic:
            if len(obj_dic[o])>1:
                for player in obj_dic[o]:
                    player.score+=5

            else:
                player = obj_dic[o][0]
                player.score+=10
    def final_scores(self):
        self.calculate_scores(self.names)
        self.calculate_scores(self.cities)
        self.calculate_scores(self.foods)
        self.calculate_scores(self.colors)

    def print_scores(self):
        for p in self.players:
            print("p:",end=" ")
            print(self.players[p].score)


class Player:
    def __init__(self,player_name,game:Esm_Famil):
        self.player_name = player_name
        self.game = game
        self.name = None
        self.city = None
        self.food = None
        self.color = None
        self.score = 0

    def set_name(self,name):
        if name[0]!=game.word:
            print("wrong")
            return
        self.name = name
        nm = self.game.names
        nm[name] = nm.get(name,[])+[self]
    def set_city(self,city):
        self.city = city
        ct = self.game.cities
        ct[city] = ct.get(city,[])+[self]
    def set_food(self,food):
        self.food = food
        fd = self.game.foods
        fd[food] = fd.get(food,[])+[self]
    def set_color(self,color):
        self.color = color
        cl = self.game.colors
        cl[color] = cl.get(color,[])+[self]

if __name__ == '__main__':
    game = Esm_Famil("a")
    while True:
        command = input()
        com = command.split()
        if com[0]=="addplayer":
            game.add_player(com[1])
        elif com[1]=="name":
            player = game.players[com[0]]
            player.set_name(com[2])
        elif com[1]=="city":
            player = game.players[com[0]]
            player.set_city(com[2])
        elif com[1]=="food":
            player = game.players[com[0]]
            player.set_food(com[2])
        elif com[1]=="color":
            player = game.players[com[0]]
            player.set_color(com[2])
        elif com[0] == "stop":
            game.final_scores()
            game.print_scores()
            break
