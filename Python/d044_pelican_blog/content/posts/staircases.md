title: Staircase Building
slug: staircase-building
categories: code-challenges
date: 2018-07-22
modified: 2018-08-11

I recently received an invitation to join a Google Foobar challenge. When I was searching "itertools" for building a Python word scrambler, the screen opened up slightly and said "You're speaking our language. Up for a challenge?" I promptly clicked the green button (I forgot the button caption) to accept.

The challenge site assigned me a first challenge, which wasn't difficult. I completed a few more challenges at a similar difficulty. The problem I'm going to talk about in this post was the most challenging for me *so far*.

This is the challenge description:
>With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER.

>Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options.

>Each type of staircase should consist of 2 or more steps. No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step. For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

    #
    ##
    21
    When N = 4, you still only have 1 staircase choice:

    #
    #
    ##
    31
    But when N = 5, there are two ways you can build a staircase 
    from the given bricks. The two staircases can have heights (4, 1) or (3, 2), 
    as shown below:

    #
    #
    #
    ##
    41

    #
    ##
    ##
    32

>Write a function called answer(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

With this problem description in mind, and since the challenge already explained how to handle the small cases like three and five, I decided to calculate how many staircase options you have if you use ten bricks:

    10 -> (9,1), (8,2), (7,3), (6,4)

But then, two of these four options can be broken down further using the larger number. The nine bricks in **(9,1)** can be broken down further to make more staircase options. The subscript is to indicate that the nine bricks originated from ten:

    9_10 -> (8,1), (7,2), (6,3), (5,4)

Notice that the first option, (8,1), won't work. If we use it, we'll end up with the staircase:

    #
    #
    #
    #
    #
    #
    #
    ###
    811

Which is not a valid option because the last two steps are the same height. So now we have a rule that if we're breaking down the larger of the two numbers in a parent option, then all of the child options' smaller numbers must be greater than their parent options' smaller number:

    #
    #
    #
    #
    #
    ##
    ###
    721

This option is valid because two, which is the smaller number in the child option of (7,2), is greater than one, which is the smaller number in the parent option.

Taking this rule and the challenge's rules, we can construct the solutions for 10 bricks:

    10 -> (9,1), (8,2), (7,3), (6,4)
    
    9_10 -> (7,2), (6,3), (5,4)
    8_10 -> (5,3)

    7_9 -> (4,3)

And we see that we have nine staircase options if we start with ten bricks. 

I thought the most straightforward way to solve this challenge was to use a recursive function that will take two arguments, a pair of staircase option values. The first would be the bricks we have remaining to build with, the larger of the two values. The second argument would be the height of the previous step:

{% highlight python %}
def calculate(remaining_bricks, last_step):
    ...
{% endhighlight %}

For a recursive function, we need a base case. While looking at the staircase options, I realized that if we take the remaining_bricks value and we divide it by the last_step value plus one, and then check if that result is less than or equal to two, we can decide if we'll be able to break down the remaining_bricks further. I haven't come up with a formal proof, yet, but it worked for all of the large and small cases I tested, so I started to use it as the base case. We return one for the base case, since there is only one option if we cannot break down the numbers further:

{% highlight python %}
def calculate(remaining_bricks, last_step):
    if remaining_bricks/(last_step + 1) <= 2:
        return 1
{% endhighlight %}

Next, we need a variable that will keep track of the total amount of options. We can simply call it **options**. For a sample of ten bricks, we'll have nine options, but according to the base case, we will only count the final child nodes. And so, we'll add an "else" statement to the base case, so that if we are not at a final child node, we'll still increment the options count by one to count the intermediate nodes:

{% highlight python %}
def calculate(remaining_bricks, last_step):
    options = 0
    if remaining_bricks/(last_step + 1) <= 2:
        return 1
    else:
        options += 1
{% endhighlight %}

Next we add the code for finding all of the breakdowns from the given parameters. We go from the range of the last_step + 1 (the new minimum) to a limit. Inside the code black, we call back the calculate function with the new brick configurations:

{% highlight python %}
for i in range(last_step + 1, limit):
    options += calculate(remaining_bricks - i, i)
{% endhighlight %}

But what is the limit? Recall: 

    10 -> (9,1), (8,2), (7,3), (6,4)
    9_10 -> (7,2), (6,3), (5,4)

So a general trend seems to be that we divide the remaining bricks by two and round up. So we'll do just that by assigning this value to **limit**, after importing math.ceil():

{% highlight python %}
from math import ceil

limit = int(ceil(remaining_bricks/2.0))

for i in range(last_step + 1, limit):
    options += calculate(remaining_bricks - i, i)
return options
{% endhighlight %}

We can then call the calculate function from our main answer(n) function. When we do the initial call of calculate(n, 0), options will be incremented by one before reaching the for loop, so we will correct for this by subtracting one from calculate(n, 0)'s result:

{% highlight python %}
def answer(n):
    return calculate(n, 0) - 1
{% endhighlight %}

Our code looks like this now:

{% highlight python %}
from math import ceil

def calculate(remaining_bricks, last_step):
    options = 0
    if remaining_bricks/float((last_step + 1)) <= 2:
        return 1
    else:
        options += 1
    limit = int(ceil(remaining_bricks/2.0))
    for i in range(last_step + 1, limit):
        options += calculate(remaining_bricks - i, i)
    return options

def answer(n):
    return calculate(n, 0) - 1
{% endhighlight %}

When I tried out this code on small numbers, I got the result fairly quickly. The problem was, it was taking too long to process answer(200). According to the challenge, answer(200) should give me an answer of about 487 million. I looked up how to speed up recursion, and a small article online said to use memoization. In Python3, this is already implemented as a decorator function as functools.lrucache. [The Python Wiki presented code for creating your own memoizer class](https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize), so I implemented a version of it:

{% highlight python %}
def memoizer(calculate_function):

    class calculation_memoizer(object):
        def __init__(self, calculate_function):
            self.calculate_function = calculate_function
            self.calculations_cache = {}

        def __call__(self, *args):
            if args in self.calculations_cache:
                return self.calculations_cache[args]
            else:
                self.calculations_cache[args] = self.calculate_function(*args)
                return self.calculations_cache[args]

    return calculation_memoizer(calculate_function)
{% endhighlight %}

I created a decorator function memoizer which would take a function as a parameter. The function returns a class initialized with the function parameter. The calculation_memoizer class creates a dictionary for storing calculations that have already been made. The __call__ magic method searches for the args of calculate() in its dictionary. If it finds those args, it will return the previously calculated value. Otherwise, It will add those arguments to the dictionary and obtain the result from calculate(args) and assign it as the value. Once I added this code, answer(200) finished in a few seconds.

You can find the source code for my solution in my [100-Days-Of-Code repo](https://github.com/yashaslokesh/100-Days-Of-Code/blob/master/Python/d015_staircase/d015_staircase.py) and in my [google-foobar repo](https://github.com/yashaslokesh/google-foobar/tree/master/level_3/the_grandest_staircase_of_them_all).

Email any questions or concerns to yashloke@terpmail.umd.edu or reach out to me on Twitter [@yashaslokesh_](https://twitter.com/yashaslokesh_) to have a discussion.
