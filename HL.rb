=begin
Riley Deal
Generate a random number and guess what the number is
Ruby is very simple to python at its base, really the only thing that is new over python is some syntax
for example, gets is similar to print, but has a build in '/n' and .to_i is a method used to convert to integers
which works because everything in ruby is an object
=end

def main()
    topEnd = 100#set the top and low end numbers for use in the math used for guessing
    lowEnd = 1
    turn = 0#number of guesses
    print "Please enter an integer within the following number range [1,100]."
    input = gets.chomp#ask the user for their number as an integer and store it in the variable correct
    correct = input.to_i#convert the string input to an integer stored in correct
    keepGoing = true#set a boolean sentry variable for while loop
    while keepGoing
        guess = (lowEnd+topEnd)/2#calculate the guess as the middle number for a given set (binary search alg)
        puts "Computer's Guess: #{guess}"
        turn += 1#increment the number of guesses
        if guess > correct#if too high drop the top end by half the number number range
            puts "Too High"
            topEnd = (lowEnd+topEnd-2)/2
            keepGoing = true
        elsif guess < correct#if too low raise the low end to 1 number above the guess
            puts "Too Low"
            lowEnd = guess+1
            keepGoing = true
        else#otherwise print correct and number of guesses it took
            puts "Correct!"
            puts "It took #{turn} guesses!"
            keepGoing = false#set sentry to false to stop loop
        end#end if
    end#end while
    puts "Exit the script with enter."#used to stop the script from auto closing
    gets
end#end main function

main()
