# the "//#" comments are not needed, it is "//" by default but there is no syntax highlighting for this
# on github, so it looks better with a hashtag.

//# functions are created using | *name* |, any addition arguments can be specified using a space afterwards, like num below
//# there is no need to deal with types, it just prints.
| doubler | num { 
    show num "doubled is" num * 2 
}

//# the "as" here is actually not needed, var count = 0 also works.
var count as 0

//# you call a function with a single ">" syntax, double ">>" are used for built in functions, 
//# such as "wait" eg. ">> wait 5" to sleep for 5 seconds
//# or ">> clear", to clear the screen
while count < 10 {
    > doubler count

    ++ count // you can increment by one using "++ *var*"
}


var arr as [1, 2, 3, 4, 5]

//# for loops work!!
for i in arr {
    show i
}
