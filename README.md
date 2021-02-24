# SiberiaSort

SiberiaSort is a modified version of a sorting algorithm that I saw in a tweet.
The idea of the original algorithm was that you whould take an array, go through it, and every element that wasn't already sorted whould be eliminated.
The algorithm was called Stalin sort and the tweet was entirely meant as a joke. This algorithm is taking the joke too far.

My algorithm makes the simple change that instead of eliminating all non-conforming elements, 
it instead puts them into a new array called a gulag and runs the algorithm recursively.
Once the algorithm finds a sorted array it merges the gulags together to create the sorted array.
I call it SiberiaSort because you whould need an entire Siberias worth og gulags to run the algorithm.
