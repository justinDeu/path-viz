# Path Finding Visualizer

This is a small program that I wrote for a Combinatorics project. The idea was to design a program that allows for the visualization of various different path finding algorithms. 

Through this project, I was able to learn more about different algorthims we discussed in the class such as [Djikstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm "Djikstra's Algorithm on Wikipedia").

In the future, I hope to expand the program to show more information and also explore further concepts within graph theory.

### To-Do List
* Add reset button
* Refactor board class to make access through functions
* Implement algo base class
    * constructor takes board to operate on
    * public step function advances through one iteration of algorithm
    * public finished function returns boolean of if it finished
    * actual algorithms use private functions called within step
* Implement Djikstra's algorithm
* Implement Error when path is impossible 