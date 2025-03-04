# TGJCO-March2025

# Blackjack Coding Challenge

## Objective

Teams must create an interactive command-line (CLI) program that plays a single round of Blackjack using the provided Deck of Cards API. Points will be awarded based on the number of correctly implemented features.


## Submission Requirements

Teams must submit a video demo (max 2.5 minutes) showcasing all implemented features.

The program must be interactive, allowing a user to play one full round against a dealer.

Winning teams will have programs manually tested by judges to verify 

## Basic Requirements (Mandatory Features)

The program must:

1. Allow one player to play against the dealer.

2. Start a round by dealing two cards to both the player and the dealer.

3. Allow the player to choose to 'Hit' (receive another card) or 'Stand' (end their turn).

4. Show the player's total after each move.

5. The dealer must hit on 16 and stand on 17 or higher.

6. Display the round's outcome:

Player wins if their total is higher than the dealer’s without going over 21.

Dealer wins if the dealer’s total is higher than the player's without going over 21.

Push (Draw) if both totals are equal.

Player loses immediately if they go over 21 (bust), without the dealer having to play.

## Additional Features (Bonus Points)



# Card Deck Simulator

## Overview

This is a simple Node.js-based HTTP server that simulates a standard deck of 52 playing cards. The server provides two endpoints:

/get-card: Draws the next card from the deck.

/shuffle: Shuffles and resets the deck.

## Prerequisites

Ensure you have Node.js installed on your system.

### Installing Node.js

If Node.js is not already installed, follow these steps:

**Download Node.js**: Visit the official website [here](https://nodejs.org/)

**Install Node.js**: Choose the LTS (Long-Term Support) version and follow the installation instructions for your operating system.

**Verify Installation**: Open a terminal or command prompt and run:

node -v

If installed correctly, this will display the Node.js version.

## Installation

Clone the repository or copy the source code to your local machine.

Navigate to the directory containing the script.

Run the following command to start the server:

node CardDeckSim.js

## Usage

Once the server is running, you can access the endpoints:

Draw a Card

To get the next card in the deck, make a GET request to:

curl http://localhost:9090/get-card

Example Response:

{
"card": "7H"
}

If the deck is empty, it returns:

{
"card": null
}

Shuffle the Deck

To shuffle and reset the deck, make a GET request to:

curl http://localhost:9090/shuffle

Example Response:

{
"message": "Deck shuffled!"
}

## Notes

The deck is automatically shuffled when the server starts.

Once all cards are drawn, /get-card will return null until the deck is shuffled again.

## License

This project is open-source and available for modification and distribution.
