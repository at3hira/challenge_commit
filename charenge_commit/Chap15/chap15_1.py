from random import shuffle

class Card:
    # クラス変数
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9",
                "10", "Jack", "Queen", "King", "Ace"] # リストのインデックス操作と値を合わせるため最初2つの要素にNoneを指定
    
    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2): # 特殊メソッド x < y
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, c2): # 特殊メソッド x > y
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        else:
            return False

    def __repr__(self): # 特殊メソッド クラス変数のsuitsとvaluesの値を返却
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck: # トランプ一式を表すクラス
    def __init__(self):
        self.cards = [] # 全52枚のカードのリスト
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j)) # Cardオブジェクトを作成し、リストに追加        
        shuffle(self.cards) #cardsリストをシャッフル

    def rm_card(self): # cardsリストの末尾の要素を一つ削除し、その要素を返す

        if len(self.cards) == 0:
            return
        return self.cards.pop()

#deck = Deck() 

class Player: # プレイヤーの情報を表すクラス
    def __init__(self, name):
        self.name = name
        self.card = None
        self.wins = 0



class Game: # ゲームクラス
    def __init__(self):
        player1 = input("プレイヤー1の名前")
        player2 = input("プレイヤー2の名前")
        self.p1 = Player(player1) # Playerクラスのオブジェクト作成
        self.p2 = Player(player2) # Playerクラスのオブジェクト作成
        self.deck = Deck() # Deckオブジェクトを作成

    def wins(self, winner): # 勝ったプレイヤーを出力
        w = 'このラウンドは　{} が勝ちました'
        w = w .format(winner)
        print(w)

    def draw(self, player1, card1, player2, card2): # 引いたカードを出力
        d = "{} は {}、{} は {}を引きました"
        d = d. format(player1, card1, player2, card2)
        print(d)

    def play_game(self): # ゲーム開始
        cards = self.deck.cards
        print('戦いを始めます')
        # デッキの残りカード枚数が2枚未満 OR ’q’を入力するとゲーム終了
        while len(cards) >= 2:
            m = 'qで終了　それ以外のキーで開始'
            response = input(m)
            if response == 'q':
                break
            
            p1c = self.deck.rm_card() # デッキからカードを1枚引く
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name

            self.draw(p1n, p1c, p2n, p2c)

            # カードの大きさを比較
            if p1c > p2c:
                self.p1.wins += 1 # Playerクラスのwins変数をインクリメント
                self.wins(p1n) # 勝ったプレイヤーを出力
            else:
                self.p2.wins += 1
                self.wins(p2n)

        win = self.winner(self.p1, self.p2) # Gameクラスのwinnerメソッド
        print('ゲーム終了{}の勝ち' .format(win)) # 勝ったプレイヤーを表示して終了
            
    def winner(self, p1, p2): # 勝った回数を比較し多い方のプレイヤー名を返す
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        else:
            return '引き分け'


game = Game() # Gameオブジェクト作成
game.play_game() # ゲーム開始
