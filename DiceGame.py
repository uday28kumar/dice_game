import random
import uuid
from Player import Player
from Dice import Dice
import sys


class DiceGame:
    def __init__(self, numberOfPlayers, targetPoint):
        self.id = uuid.uuid4()
        self.name = "Dice Game"
        self.numberOfPlayers = numberOfPlayers
        self.targetPoint = targetPoint
        self.players = self.__initPlayers(numberOfPlayers)
        self.dice = Dice()
        self.nextPlayer = 0
        self.currentOpenRank = 1

    def __initPlayers(self, n):
        players = []
        for i in range(n):
            players.append(Player("Player-"+str(i)))

        random.shuffle(players)
        return players

    def __isGameOver(self):
        count = 0
        for player in self.players:
            if(player.points >= self.targetPoint):
                count = count + 1

        if count == self.numberOfPlayers:
            return True

        return False

    def showRankBoard(self):
        sortedPlayers = sorted(self.players, key=lambda x: x.rank)
        print("*****************Rank Board*****************")
        print("Rank\t|Player Name\t\t|Score")
        print("-----\t-----------\t\t------")
        for player in sortedPlayers:
            displayRank = str(player.rank)
            if player.rank == 9999999999:
                displayRank = 'N/A'

            print(displayRank+"\t|"+player.name+"\t\t|"+str(player.points))
            print("-----\t-----------\t\t------")

    def play(self):
        print("Order of players is: ")
        for player in self.players:
            print(player.name)

        while not self.__isGameOver():
            currentPlayer = self.players[self.nextPlayer]
            if(currentPlayer.havePanality is True or currentPlayer.points >= self.targetPoint):
                if currentPlayer.havePanality is True:
                    self.players[self.nextPlayer].lastPoint[0] = 0
                self.nextPlayer = (self.nextPlayer + 1) % self.numberOfPlayers
                continue

            if currentPlayer.haveBonusChance is True:
                input(currentPlayer.name +
                      " Got another chance (Roll the dice again): ")
            else:
                input(currentPlayer.name +
                      " It's your turn(press enter(<-') to roll the dice):- ")

            value = self.dice.roll()
            print(value)
            currentPlayer.addPoint(value)
            if currentPlayer.haveBonusChance:
                self.nextPlayer = (self.nextPlayer + 1) % self.numberOfPlayers

            if currentPlayer.points >= self.targetPoint:
                currentPlayer.rank = self.currentOpenRank
                self.currentOpenRank = self.currentOpenRank + 1

            self.showRankBoard()


n = int(sys.argv[1])
target = int(sys.argv[2])
diceGame = DiceGame(n, target)
diceGame.play()
