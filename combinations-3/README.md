20 minutes to complete. About 5 of that was boiler code. 5 was debugging.

I made a mistake reseting the start of the array after a decrement, again.

It was this:

I wanted range(i-1, -1, -1) but I wrote range(i-1, 0, -1). Darn. This means that you never execute for
j = 0. And that means that 'recent[0]' never gets set to one less than 'recent[1]'. The iteration variable
is over indices in 'recent' that you want to reset to one less than the following element.