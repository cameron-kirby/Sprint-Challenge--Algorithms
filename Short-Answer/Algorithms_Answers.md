#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) BigO(n)
Contains a while loop that has complexity on a linear scale

b) BigO(n^2)
Contains a nested for/while loop, therefore bringing up the complexity to a quadratic scale

c) BigO(n)
Recursive algorith, that basically decrements n, the number of bunnies, and counts the ears of the bunnies removed in this way. It's linear

## Exercise II

1) Begin at the middle floor of the building, and drop an egg
2) if the egg is broken, go to middle floor between current floor and bottom floor and drop an egg
3) if it survives the fall, go to middle floor between current and top floor and drop an egg
4) repeat 2 and 3 until egg breaks from current floor

This formula would iterate through the floors until the lowest floor that broke the egg was located. The number of floors, n, is divided in half at each iteration, making the overall complexity of this forumla BigO(log n)

