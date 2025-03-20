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
uv venv --python 3.13 .venv
. .venv/Scripts/activate # windows
. .venv/bin/activate # bash
uv run --script src/tgjco_march2025/main.py --with requests --with rich
```

#### Running the code

To run our code you can execute `main.py` to enter the gameplay loop the player and dealer will be dealt 2 cards and you will be prompted to Hit or Stick until the game is over and either the dealer or player has won.

note: handling Ace's since aces can be both Low or High drawring and Ace will double the length of the scores list to keep track of both the low and high score.