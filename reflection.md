# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  -the hints when given said that it was low and that you should go lower or that when 
  you put it higher than secret it will tell you to even higher 
  - another bug is when you change the difficulty the range is defaulted to 1 to 100 so change in 
  difficulty doesn't matter 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |Go lower            Go higher          Too high! GO higher  
| | | | |1 to 20             1 to 100          1 to 100 
| | | | |secret = 13          secret = 15        

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used deepseek and Claude code for this project 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One of the ai suggestions was that they said was New Game Doesn't Reset Correctly as 
when the user wants to start a new game has inconsistent state attempts as well 
as the secret number being hard coded to be between 1 and 100

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
There is one part of the AI suggestion where they were halluicating that there is a bug in the suggestion
in which they thought that the hint messages are swapped despite me fixing the bug when I gave them the code to check 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decide whether a bug was really fixed is when I run the program again and see if that bug
that was there is gone now 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  one test I run was to check if the secret number changes when I change difficulty and what it showed about my code is that there were things that I had to add in order to fix that bug 

- Did AI help you design or understand any tests? How?
yes as everytime there was a bug that appear they would give reasons for why this bug is wrong and how it should be fixed and for each fix I would manually test that area of the code to see if it is fixed 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
The idea of Streamlit is imagine ordering a coffee from a robot barista. a normal python script would make it so that once you run it the robot makes your coffee order and is done with it. In a streamlit The robot watches you through a window. Every time you change your order (click a button, type something, select an option), it throws away the old coffee and makes a fresh one based on your new order.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habit I want to reuse or do in future labs or projects is to manually read through the code so I can gain better understanding of the code thus helping me reduce token usage when I run it through ai 
- What is one thing you would do differently next time you work with AI on a coding task?
One thing I would do differently next time is to rely on myself for readingcode more next time 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
One thing I learn about ai generated code is that it can reduce the time I write code and allows me to spend more time debugging it rather than just writing it all from sratch 
