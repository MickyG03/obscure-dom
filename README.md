# obscure-dom

The program reduces the dom elements dimensions
I have used python and bs4 library alongwith regex which helped me to easilly remove the none essential components of html files.


## Results:

Based on the rl given in the task: https://github.com/kaavee315
the program reduces the dom elements by almost 20% (18.19%)

the output of the final file can be seen in output.html

No. of elements before: 2276
No. of elements after reduction:1862

## Why Python:

Easy to use, bs4 and regex library makes things alot easier, faster, and provides smooth commute between AI programs that uses python.

## Input:

the program directly takes the html file as input.

## what it does:

1. Removes the comments.
2. Removes the meta tags, as meta tags aren't important. Though they provide description about a tag, but for training LLMS, meta tags may hinder the process.
3. Removes the styles and scripts.
4. Removes hidden elements.
5. Groups the elements by role if there's any.