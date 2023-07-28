#include <cstdlib>
#include <iostream>
#include <time.h> 
using namespace std; 
  
 //int myNum = 5;                Integer (whole number without decimals) 
 //double myFloatNum = 5.99;     Floating point number (with decimals) 
 //char myLetter = 'D';          Character 
 //string myText = "Hello";      String (text) 
 //bool myBoolean = true;        Boolean (true or false) 
  
 //rock paper scissors 

int main()
{
				
     //Describes user input and telling him what he can choose
     int user_input; 
     cout << "Choose one of options: \n"<< 
             "- Type 1 for rock \n" << 
             "- Type 2 for paper \n" << 
             "- Type 3 for scissors\n"; 
  
     cin >> user_input; 
  
  
  
     //if user typed 1, 2 or 3 it will print what he choosed 
     if (user_input == 1) 
     { 
         cout << "you choosed: rock \n"; 
  
     } else if (user_input == 2) 
     { 
         cout << "you choosed: paper \n"; 
     } else if (user_input == 3) 
     { 
         cout << "you choosed: scissors \n"; 
     } 
  
  
  
     // Ai move : 
     int ai_move = 0; 
  
         srand(time(0)); 
         ai_move = (rand() % 3 + 1); //make a random number between 1 and 3 
  
     //print what ai generated 
     if (ai_move == 1) 
     { 
         cout << "my move is: rock \n"; 
  
     } else if (ai_move == 2) 
     { 
         cout << "my move is: paper \n"; 
     } else if (ai_move == 3) 
     { 
         cout << "my move is: scissors \n"; 
     } 
  
  
  
     //Check if user won or Ai 
     string win = "you won, ai on bottom"; 
     string loose = "you loose, AI WON !!!"; 
  
     if (user_input == 1 and ai_move == 2)  
     { 
         cout << loose;   
     } 
     else if (user_input == 1 and ai_move == 3) 
     { 
         cout << win; 
     } 
     else if (user_input == 2 and ai_move == 1) 
     { 
         cout << win;     
     } 
     else if (user_input == 2 and ai_move == 3) 
     { 
         cout << loose; 
     } 
     else if (user_input == 3 and ai_move == 1) 
     { 
         cout << loose; 
     } 
     else if (user_input == 3 and ai_move == 2) 
     { 
         cout << win; 
     } 
     else if (user_input == ai_move) 
     { 
         cout << "its a tie, try again"; 
     } 
    return 0;
}