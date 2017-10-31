# Introduction #
firstDraft was my first foray into TDD. It was a fascinating experience, to put it simply.
Below I want to discuss what went well, what didn't, and what I didn't expect.

## Slow Down! ##
My first observation from doing TDD is that I coded a _lot_ more slowly than
I typically do. I estimate it took me about 40 hours to write this whole program,
as opposed to the 12 it took to do the similar project B[racket]B[uilder]. 
A very small portion of this is due to the extra typing attributed to the tests. 
The biggest speed hump was the planning process. One of the tenets 
of TDD is that you write a test first to check functionality of something.
Only then do you write your real code, and only enough code to have that test pass. 
No overengineering. No overplanning methods with too much functionality. 
In short, I had to put a lot more thought into what I wrote before writing it,
for better or for worse. (I'd say mostly for the better, as I'll explain below).

## Encapsulation ##
Another tenet is that tests should be independent of each other. In short,
one test or feature failure should not cause all other tests to fail. 
While I cannot say that I have mastered purely independent tests, my efforts 
to meet this requirement forced me to think much more deeply about important 
OO principles, like encapsulation. The testing nature made me much more conscious
about where I put certain methods and attributes. Now, I am much more careful 
about my methods handling all changes to themselves.

## Maintainability ## 
The most obvious benefit of TDD is that by the end, you have tests already
written for all of your methods. This has proven very helpful as I write more 
modular code. It is a lot easier to track down an issue in a multiple-file
project when you can simultaneously run tests for all of them.

## Conclusion and next steps ##
All in all, I think TDD was a good choice. I feel like my project is more thought
out and will be easier to refactor in the future. (I plan to reuse much of the
codebase to make a similar program for other fantasy sports.) I'll probably
continue using this technique for medium to large projects I do.

The speed slowdown is a big hurdle to overcome, though.

Next steps will be to learn to use Mock objects better, brush up on
OO Design even more, and just keep coding. I'd lke to web host this project.
Frankly, adding some HTML UI will probably make the inputs much easier to handle
on the backend. (The inputs are a bit wonky currently, since they interfere with
the unittests.)