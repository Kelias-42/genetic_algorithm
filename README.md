# Project description
This is a basic application of a genetic algorithm in order to find a targeted sentence.

This project aims to recreate real life mechanisms such as natural selection and mutations in a code environment.

At first, it starts a with a randomly-generated population made from strings that have the same length as the target.

The goal is to have this population evolve over generations in order to have a member equal to the target.

In order to do that, the generated sentences will get a fitness score based on how much characters they have in common with the targeted sentence (position matters).

The higher the score, the more likely they are to be picked to become parents in the next generation.

Each generated child will be made-up from their parents characters.

There is also a fixed chance that a generated child will have mutations, meaning that any of their characters may be replaced by another randomly generated character.

# Constants
You can try to change the constants like the target, the mutation rate of the population size at the beginning of the program and see what impact it will have.

For the targeted sentence, you may only use capital characters and spaces.

# Credits
This project was made for learning purposes, it has a lot of shortcomings and is not particularly useful but it made me learn a lot and I had a blast doing it.

It was widely inspired by the teachings of Daniel Shiffman on his YouTube channel known as The Coding Train.

Here is his playlist on genetic algorithms: https://www.youtube.com/playlist?list=PLRqwX-V7Uu6bJM3VgzjNV5YxVxUwzALHV
