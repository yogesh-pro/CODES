#include <iostream>
#include<string>
using namespace std;

void update_board(string board[]){
    cout<<"\n";
    cout<<board[0]<<"|"<<board[1]<<"|"<<board[2]<<endl;
    cout<<"-----"<<endl;
    cout<<board[3]<<"|"<<board[4]<<"|"<<board[5]<<endl;
    cout<<"-----"<<endl;
    cout<<board[6]<<"|"<<board[7]<<"|"<<board[8]<<endl;//created by : Saurabh Sa//created by : Saurabh Saini
    cout<<"\n";
}
int take_input(int user){
    int move;
    if(user==0){
        cout<<"X's Move : ";
        cin>>move;
    }
    else{
        cout<<"O'move : ";
        cin>>move;
    }
    return move;
}
string fill_in_board(int move,string player,string board[]){
    board[move] = player;
    return board[move];
}
string check_win(string player,string board[]){
    if((board[0]==player && board[1]==player && board[2]==player)||
    (board[3]==player && board[4]==player && board[5]==player)||
    (board[6]==player && board[7]==player && board[8]==player)||
    (board[0]==player && board[3]==player && board[6]==player)||
    (board[1]==player && board[4]==player && board[7]==player)||
    (board[2]==player && board[5]==player && board[8]==player)||
    (board[0]==player && board[4]==player && board[8]==player)||
    (board[2]==player && board[4]==player && board[6]==player)){
        return player;
    }
    else{
        return " ";
    }
}

int main(){
    string board[9] = {"0","1","2","3","4","5","6","7","8"};
    int user = 0;
    int move;
    string player;
    string winner=" ";
    int counter=0;
    while(true){
        counter++;
        if(counter==9){
            cout<<"draw";
            break;
        }
        update_board(board);
        move = take_input(user);
        if(user==0){
            player = "X";
        }
        else{
            player = "O";
        }
        fill_in_board(move,player,board);
        winner = check_win(player,board);
        if (winner!=" "){
            cout<<winner<<" is winner";
            break;
        }
        user = (user+1)%2;
    }
    return 0;
}