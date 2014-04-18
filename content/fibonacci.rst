**Iteration** and **Recursion** in **Python**
#################################################

:date: 2014-04-10 14:56
:tags: Fibonacci, python, iterative, recursion
:category: Home
:slug: Fibo
:author: **Gina Schmalzle**
:page-order: 1
:summary: **Iteration vs. Recursion in Python**

**Iteration vs. Recursion in Python**
======================================

For the past week at Hacker School, I took a step back from making a cool and awesome projects like the `Vector Projector  <http://geodesygina.com/vectorprojector/vectorprojector.html>`_  or the `Japan Earthquake  <http://geodesygina.com/vectorprojector/vectorprojector.html>`_ projects and looked at some good, old-fashioned computer science concepts. Much of what I did was repetive; I found a really simple problem, solved it using some method, and then tried solving it again using a variety of other methods.  One project I worked on was programming the  n'th **Fibonacci** number using **python**. In this blog I will describe **iterative** and **recursive** methods for solving this problem in Python. 

What are **Fibonacci** numbers (or series or sequence)?  From `the Fibonacci Wiki Page  <http://en.wikipedia.org/wiki/Fibonacci_number>`_, the Fibonacci sequence is defined to start at either 0 or 1, and the next number in the sequence is one.  Each subsequent number in the sequence is simply the sum of the prior two.  Hence the Fibonacci sequence looks like:: 
 
 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

or::

 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

It is mathmatically defined as::

 F(n) = F(n-1) + F(n-2)


My first approach was an **iterative** method -- basically, hardwire the case for F(0) and F(1), and then iteratively add the the values for larger values of n:: 

  def F_iter(n):
        if (n == 0):
                return 0
        elif (n == 1):
                return 1
        elif (n >1 ):
                fn = 0
                fn1 = 1
                fn2 = 2
                for i in range(3, n):
                        fn = fn1+fn2
                        fn1 = fn2
                        fn2 = fn
                return fn
        else:
                return -1


OK, great, this works just fine...  Now, let's try writing this recursively.  You may ask, what is recursion in computer science? -- I certainly did about a week ago.  **Recursion**, according to `the Recursion Wiki page  <http://en.wikipedia.org/wiki/Recursion_(computer_science)>`_ is a method where the solution to a problem depends on solutions to smaller instances of the same problem. Computer programs support recursion by allowing a function to call itself (Woa! -- this concept blew my mind).  

A **recursive** solution to find the nth **Fibonacci** number is::

   def F(n):
        if (n == 0):
                return 0
        elif (n == 1):
                return 1
        elif (n > 1):
                return (F(n-1) + F(n-2))
        else:
                return -1

Notice that the recursive approach still defines the F(0) and F(1) cases.  For cases where n > 1, however, the function calls itself.  Let's take a look at what is happening here. Suppose we call F(4). F(4) will forgo the n = 0 and n = 1 cases and go the the n > 1 case where it calls the function twice with F(3) and F(2).  F(3) and F(2) then each subsequently call the function again -- F(3) calls F(2) and F(1), and F(2) calls F(1) and F(0), as shown in the tree structure below (**Figure 1**).  The F(1) and F(0) cases are the final, terminating cases in the tree and return the value of 1 or 0, respectively. So, just as Wikipedia said, the recursive case breaks down the problem to smaller instances, and it does that by allowing the user to define a function that calls itself:

.. raw:: html	    
	:file: tree.html

*Figure 1. Tree structure demonstrating the recursion flow for a case where n = 4.  Figure made using* `D3.js <http://d3js.org/>`_.

Fantastic!  Now we have both the iterative and recursive styles of this code, and we can now see how recursive coding works.  Playing around with these codes, however, I noticed that the run time on the recursive case was MUCH slower than the iterative case for large n.  I included a timer (time.time()) to measured how quickly each run is estimated for a range of n.  What I got is a figure that looks like this:

.. raw:: html       
        :file: fibo_time.html

*Figure 2. Run times for calculating a range of n (0-25) using the iterative (blue) and recursive (red) approaches. Figure made with* `mpld3 <http://mpld3.github.io/>`_.  

Where the red line represents recursive times and the blue iterative times. For small values of n the two methods are relatively the same, but for large values of n the time really starts to lengthen for the recursive case!  So, why is this?  Let's take another look at **Figure 1**.  The tree structure shows that the F(4) and F(3) cases are only calculated once, but each subsequent case is calculated multiple times!  For example, the F(1) case is calculated 3 times!  Hence, the recursive method calculates the same thing multiple times, wasting valuable run time.   

So why use recursion? Well, the recursive code is a lot easier to read. For the n > 1 case, the mathematical equation is explicitly written out, whereas in the iterative case the programer has to step through the script to understand what is going on.  But the obvious gorilla in the room is that recursion in python is REALLY slow.  **Memoization** (pronounced like Elmer Fud trying to say memorization) is a technique used to deal with this problem.  Memoization and memorization are kind of synonomous in this case -- we want to make the program 'memorize' the result from previous runs. These memorized runs will be used for subsequent, repeated calls.   We do this by assigning the value to a hash table.  This involves a simple modification of the code::

   mem = {}
   def F_mem(n):
        if (n == 0):
                return 0
        elif (n == 1):
                return 1
        elif (n > 1):
                if n not in memo:
                        memo[n] = (F_mem(n-1) + F_mem(n-2))

                return memo[n]
        else:
                return -1  

Now, let's run our timer again, but this time use the memoized recursion:

.. raw:: html       
        :file: fibo_time_mem.html


*Figure 3. Run times for calculating a range of n (0-200) using the iterative (blue) and memoized recursive (red) approaches. Figure made with* `mpld3 <http://mpld3.github.io/>`_.  

Woa!  As `Mary Rose Cook <http://maryrosecook.com/>`_ would say, "Now we're cookin' with gas."  Run times for the recursive method are now out-pacing the iterative method!  So, by memoizing your recursive function you can get your code to run REALLY fast!  A down side to this, however, is that you are going to take up memory by storing information in your hash table.

Hope you liked my blog!  'Till next time!
