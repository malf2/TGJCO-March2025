var http = require('http');

class Deck {
    constructor() {
        this.suits = ["H", "D", "C", "S"];
        this.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"];
        this.cards = [];
        this.shuffle();
    }

    shuffle() {
        this.cards = [];
        for (let suit of this.suits) {
            for (let rank of this.ranks) {
                this.cards.push(`${rank}${suit}`);
            }
        }
        this.cards.sort(() => Math.random() - 0.5); // Shuffle deck
        console.log("Deck shuffled!");
    }

    getCard() {
        return this.cards.length > 0 ? this.cards.pop() : null;
    }
}

const deck = new Deck();

http.createServer(function (req, res) {
    let response;
    if (req.url === "/get-card") {
        const card = deck.getCard();
        response = JSON.stringify({ card: card ? card : null });
    } else if (req.url === "/shuffle") {
        deck.shuffle();
        response = JSON.stringify({ message: "Deck shuffled!" });
    } else {
        res.writeHead(404, {'Content-Type': 'application/json'});
        res.end(JSON.stringify({ error: "Endpoint not found" }));
        return;
    }
    res.writeHead(200, {'Content-Type': 'application/json'});
    res.end(response);
}).listen(9090, () => {
    console.log("Server running at http://localhost:9090/");
});
