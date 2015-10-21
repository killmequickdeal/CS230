#include <iostream>
#include <string>
#include <time.h>
#include <cstdlib>
#include <limits.h>//included in order to use INT_MIN and INT_MAX for error handling
using namespace std;

//Riley Deal C++ Guessing Game for CSCI 240
//Have a computer guess the users number in 7 tries or less

int turn = 0;//start at 0 turns or "guesses"
void basicguess();//create void equations for reference in main
void blackbeltguess(int correct);

int main(){
	int correct;//placeholder initialization for the users input number 
	bool keepGoing = true;//sentry variable for while loop
	int gameMode;//placeholder variable for running the chosen function
	while(keepGoing){//while loop for checking integrity of user input
		cout << "Please enter an integer in the following set [1,100] " << endl;
		cin >> correct;//take a users number
		if (correct >= 1){//check if number is greater than 1, thus eliminating negatives
			if (correct <= 100){//check if number is under 100 eliminating positives over 100 and symbols, etc.
			cin.clear();
			cin.ignore(INT_MAX, '\n');//clear the console and ignore anything extra as a precautionary measure(for decimals as the extra decimal number is used as next input)
			cout <<"DISCLAIMER: after error handling your number is: " << correct << endl;//let the user know if their number was changed
			cout << "Thank You" << endl;
			keepGoing = false;//stop while loop
			}else{
			cout << "Invalid Input" << endl;//if final criteria are not met tell the user and prompt for re-entry
			cin.clear();
			cin.ignore(INT_MAX, '\n');//clear and ignore as before as extra precaution
			keepGoing = true;
			}//end inside if
		}else{//did not pass initial test, ask for re-entry 	
		cout << "Invalid Input" << endl;
		cin.clear();
		cin.ignore(INT_MAX, '\n');//clear and ignore as before
		keepGoing = true;
		}//end outside if
	}//end while loop
	cout << "I will now attempt to guess your number in 7 tries or less!" << endl;
	cout << "Press 1 for user input" << endl << "Press 2 for automated program" << endl;//give user the game modes
	while(keepGoing==false){//use the same sentry variable from the beginning of main, but reversed to stop when true for simplicity
		cin >> gameMode;//take input game mode from user
		if(gameMode == 1){
		cin.clear();
		cin.ignore(INT_MAX, '\n');//clear and ignore as before
		keepGoing = true;
		basicguess();//go to user input function and end loop
		}else if (gameMode == 2){
		cin.clear();
		cin.ignore(INT_MAX, '\n');//clear and ignore as before
		keepGoing = true;
		blackbeltguess(correct);//go to automated function and end loop, correct is passed in for use in comparison
		}else{
		cin.clear();
		cin.ignore(INT_MAX, '\n');//clear and ignore as before
		cout << "Invalid Input" << endl;
		keepGoing = false;//if input is invalid continue loop
		}//end if
	}//end while loop 	
	cout << "It took " << turn << "turns." << endl;//print how many guesses it took
	
}//end main

void basicguess(){		
	int topEnd = 100;//set top end and low end numbers for math use 
	int lowEnd = 1;
	bool keepGoing = true;//sentry variable for while loop
	cout <<  "Is my guess high(h), low(l), or correct(c)?" << endl;//prompt user to answer in the correct ways
	
	while(keepGoing){
		turn++;//increase guess count
		int guess = (lowEnd + topEnd)/2;//make the computer guess as the middle number (binary search algorithm)
		string horl;//set string which will store user input
		cout << turn << ": My guess is: " << guess << endl;
		cin >> horl;//take in user input
		if (horl == "l"){//if guess is too low increase the lowest possible number to 1 higher than the guess
		lowEnd = guess+1;
		} else if (horl == "h"){//if guess is too high set the highest as the number exactly between current lowest and highest, account for possible decimals
		topEnd = (lowEnd + topEnd-2)/2;
		} else if (horl == "c"){//if correct end while loop
		cout << "Correct!" << endl;
		keepGoing = false;
		}else{//account for user being incompitent as always. Hopefully no decimals here since it is a letter input instead of numbers
		turn--;//decrement the amount of guesses and this will not count as one
		cout << "That is not a valid input, retry" << endl;
		}//end if 
	}//end while
}//end search

void blackbeltguess(int correct){//pass in correct for comparison
	int topEnd = 100;//set top and low end numbers for math use
	int lowEnd = 1;
	bool keepGoing = true;//sentry variable for while loop

	while(keepGoing){
		turn++;//increase guess count each time computer loops through
		int guess = (lowEnd + topEnd)/2;//make the computer guess as the middle number (binary search alg)
		cout << turn << ": My guess is: " << guess << endl;
		if (guess < correct){//print computer guess and automatically compare it versus the passed in correct value
		cout << "Too low" << endl;
		lowEnd = guess+1;//if guess is too low increase the lowest possible number to 1 higher than the guess
		} else if (guess > correct){
		cout << "Too high" << endl;//if guess is too high set the highest as the number exactly between current lowest and highest, account for possible decimal
		topEnd = (lowEnd + topEnd-2)/2;
		} else{
		cout << "Correct!" << endl;//if it is not too low or too high, it must be the same number and therefore is correct
		keepGoing = false;//stop loop
		}//end if 
	}//end while
}//end blackbeltguess
