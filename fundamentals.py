# Today's warm up will consist of my personal technique for breaking dow a line of code and understanding what is happening eactly.

# This has helped me personally with understanding logic flows and user defined functions.

#1 | Using notations for personal understanding

# this is our variable we made to hold the number of the index position we want to know
index_position = 0

# we  use a for loop to say for the element in the string 'xyz', do this.
for letter in 'xyz':
    # what we do in the for loop is say print (then your string).
    # In this case we are using .format and placing our original variable which is index_position
    # And we say print the element we are iterating through by saying for letter in our string
    print('At index {} the letter is {}'.format(index_position, letter))
    # now we say our variable index_position = index_position + 1. A quick way to do that is say +=.
    index_position += 1


#2 | Breaking down range function

# a for loop that says for num/elements in range (which we set to be from 0 to 19)
for num in range(0, 20):
    # print the elements
    print(num)
# range includes everything up tot he number you list. In this case we say 20 but range only goes up to 19.
# a way to combat this is to say your rang +1.

#3 | Listing a range

# first we use the print function to see what our output is in our IDE.
# then we use list to convert our range of arbitrary numbers in to a list.
# then we use range to specify our range of numbers
# Then we say at starting point 0, through 10 plus 1, at a step of 2.
# we added + 1 to the 10 position to get the full 10 integers.
# lastly, we say count this range of 10 integers by a step of 2.

print(list(range(0,10 +1,2)))

# This technique might seem tedious, but it will help expose what you do not know.
# If you can't explain something that is happening in a line of code you wrote, it okay.
# Take the time to find the correct terminology.
# This will help you be able to explain your code better to others, as well as, understand what others are trying to teach.
