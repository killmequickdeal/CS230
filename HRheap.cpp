//Create a Program that simulates a horse race
//Riley Deal Horse Race OOP for CSCI24000
#include <iostream>
#include <string>	//include libraries necessary (such as sstream
#include <time.h>	//for printing the track and cstdlib/time to 
#include <cstdlib>	//generate random numbers
#include <sstream>

using namespace std;

//create class horse based on uml diagram
class Horse {
private:
	int position;
	int pChance;
public:
	Horse();
	void advance();
	int getPosition();
	void setPchance(int pChance);//make new setter that can set the percent chance of horse moving
};//end Horse

//default constructor
Horse::Horse(){
	Horse::position = 0;
	Horse::pChance = 2;//default 50-50 chance
}//end default constr

void Horse::advance(){
	if((rand()%pChance) == 0){//0 is used as it is the only value always available, for all values pChance
	Horse::position += 1;
	}
}//end advance

int Horse::getPosition(){
	return position;//getter
}//end getPos

void Horse::setPchance(int pChance){//setter for changing the percent change of horses moving
	Horse::pChance = pChance;
}//end setPchance

//create class Race based on uml diagram
class Race {
private:
	Horse *h;//pointer to heap data
	int length;
public:
	Race();
	Race(int length);
	~Race();
	void printLane(int horseNum);
	void start();
};//end Race
//default constructor
Race::Race(){
	Race::length = 25;
}//end default constr
//constructor with parameters
Race::Race(int length){
	Race::length = length;
}//end constr

Race::~Race(){//create destructor for heap data
	delete[] h;
}//end destructor

void Race::printLane(int horseNum){//create a stringstream in order to
	ostringstream track; //concatonate variables and strings
	for(int i=0; i<length; i++){
		if(i==h[horseNum].getPosition()){
		track << horseNum;//if the piece of track being placed equals to horse
		}else{//position, print position instead
		track << ".";//otherwise print track	
		}//end if	
	}//end for
	cout << track.str() << endl;//print track
}//end printLane


void Race::start(){
	srand(time(NULL));//seed rand with time to get different outcomes			
	h = new Horse[5];//create array of horses on heap
	int turns =0;//used to show how many passes
	int odds;//to change the odds of the horses one at a time use the for loop and setter for pChance
	bool keepGoing = true;
	for(int i=0; i<5; i++){
		cout << "Enter the odds of horse " << i <<" moving, in the set of all integers given by x>=1 (used as 1/input number)" << endl;
		cin >> odds;
		h[i].setPchance(odds);//set percent chance of horse moving to the given odds
	}
	while(keepGoing){//loop through the 5 horses until one wins
		for(int i=0; i<5; i++){//for loop for size of array of horses
			h[i].advance();//advance each horse
			printLane(i);//print each horses lane
			if (h[i].getPosition() == length){//check for a winner
			cout <<"Horse "<< i << " wins!" << endl;
			keepGoing = false;//set bool true to end while
			}//end if		
		}//end for
		cout << "Press enter for another turn:" << endl;
		turns += 1;
		cout << "Turn: " << turns << endl;
		cin.ignore();//wait for user input but ignore it
	}//end while
}//end start	


int main(){
	int distance;//used to set length of race class
	cout << "Please enter the race length in the set of all integers given by x>=1" << endl;
	cin >> distance;
	Race race = Race(distance);//create an instance of race class
	race.start();//use the race start method which will run itself until the end
}//end main		
