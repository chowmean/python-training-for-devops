# Best practices for programming and python

* Add readability to your code as much as possible. 
* Function name should tell what this function does. 
	* Function should be visible in one screen. You should not scroll to view the whole function.
	* Try to write pure funtions instead of impure functions. [Read here about pure and impure functions](https://www.learnsteps.com/pure-impure-functions/)
* One function should do one thing and that thing properly.
* Logging is very important. 
	* You should chose level of logging very wisely. Lot of logging will make your application slow. 
	* Less logging you may miss out required info for debugging. 
* Failures are normal. Fail as early as possible and as loud as possible. 
* Metrics provides you with a way to keep track what your code is working with respect to how it was working earlier. 
* Try to structure your code in such a way that if you want to add something new you can do it in minimum effort. 
* Documentation is very important. Try to document project you are about to build in advance this will make your thought clear about what you are going to make and how you will achieve it. 
* Comment wherever is necessary. You comments will help the person who will take over code to understand it easily. 
* You program should be config driven. Don't hardcode anything in your code. 
* Test cases are very important. 
	* You will have confidence in your code and less bug will go to production. 
	* Edge cases are important to consider. 
	* There are people who actually do test driven development. This means they write the test case first for what they want to achieve and then they write the code for it. 
* Always think that your software may need to interact with other software in future so write it in a way that others can interact with it. 