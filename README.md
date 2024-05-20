# Setup
1. Download the repository `MasterMind` 

2. In terminal, navigate to the folder and run mastermind with the following
```bash
cd MasterMind
python mastermind.py
```

3. Start entering your guesses and play!

# Tips
- good means the number and position of the number are correct
  e.g. the code is 1234 and you typed 1256, there will be two good numbers (1, 2)

- good number but in wrong position means the number is correct but it is in the wrong position
  e.g. the code is 1234 and you typed 3452, there will be three good numbers but in wrong position (3, 4, 2)

- the code will not have any repeated numbers
  e.g. the code is 1234, not 1223
