### Matheus, Connor and Thomas 

To run our script, you need python 3.13:

You can see where your python is and the version here:

```bash
which python
python --version
which python3 
python --version
```

If not, you can install python 3.13 manually, or with uv:

- https://docs.astral.sh/uv/getting-started/installation/

With uv installed and added to your path:

```bash
uv run --script https://gist.githubusercontent.com/tferns-ch/f05f178de596fc0ab5cdba7aa5c269c9/raw/7b6b6d50bc331d14cb813eb83d01d2be2f4b06a1/test.py
```

#### Running the code

To run our code you can execute `main.py` to enter the gameplay loop the player and dealer will be dealt 2 cards and you will be prompted to Hit or Stick until the game is over and either the dealer or player has won.

note: handling Ace's since aces can be both Low or High drawring and Ace will double the length of the scores list to keep track of both the low and high score.