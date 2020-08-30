#include <iostream>
using namespace std;
int number,x,y,a,b,mtx[10000][10000],ver1[10000][10000],ver2[10000][10000];
void showMeTable(){ //shows current table
	//for(int i = 0; i<x;i++){
	//	for(int j = 0; j<y; j++){
	//		cout<<mtx[i][j];
	//	}
	//	cout<<endl;
	//}
	int len = x-1;
	number = mtx[x-1][b];
	cout<<len<<" "<<number<<endl;
}
int main(){
	//cin>>x>>y>>a>>b; // user inputs table size (x,y) and position y positions (a,b)
	x = 8;
	y = 8;
	a = 5;
	b = 5;
	a-=1;
	b-=1;
	if(x == 2){
		cout<<"1 1";
	}
	else{
	mtx[0][a] = 1; //sets a point in main matrix
	mtx[x-1][b] = 1; //sets b point in main matrix
	ver1[0][a] = 1; //sets a point in ver1 matrix
	ver1[x-1][b] = 1; //sets b point in ver1 matrix
	ver2[0][a] = 1; //sets a point in ver2 matrix
	ver2[x-1][b] = 1; //sets b poing in ver 2 matrix
	for(int i=0; i<x; i++){
		for(int j=0; j<y; j++){
			if((i==0) and (mtx[i][j]==0)){ //marks unusable spots
				mtx[i][j] = -1;
				ver1[i][j] = -1;
				ver2[i][j] = -1;
			}
			if((i==x-1) and (mtx[i][j]==0)){ //marks unusable spots
				mtx[i][j]=-1;
				ver1[i][j] = -1;
				ver2[i][j] = -1;
			}
			if((mtx[i][j] != 1) and (mtx[i][j] != -1)){ //marks usable spots for a point
				if(((ver1[i-1][j-1] == 1) or (ver1[i-1][j] == 1) or (ver1[i-1][j+1] == 1)) or ((ver1[i-1][j-1] == -2) or (ver1[i-1][j] == -2) or (ver1[i-1][j+1] == -2))){
					ver1[i][j] = -2;
				}
			}
		}
	}
	for(int i=x-1; i>0; i--){
		for(int j=0; j<y; j++){
			if((mtx[i][j] != 1) and (mtx[i][j] != -1)){ //marks usable spots for b point
				if(((ver2[i+1][j-1] == 1) or (ver2[i+1][j] == 1) or (ver2[i+1][j+1] == 1)) or ((ver2[i+1][j-1] == -2) or (ver2[i+1][j] == -2) or (ver2[i+1][j+1] == -2))){
					ver2[i][j] = -2;
					if(ver1[i][j] == -2 and ver2[i][j] == -2){ //is spot is usable for both (a and b) points marks it in main matrix
						mtx[i][j] = -2;
					}
				}
			}
			if(mtx[i][j] == 0) // marks all leftover spots as unusable
				mtx[i][j] = -1;
		}
	}	
	for(int i=1;i<x-1;i++){
		for(int j=0;j<y;j++){
			if(mtx[i][j] == -2){
				mtx[i][j] = 0;
				if(mtx[i-1][j-1] > 0){
					mtx[i][j] += mtx[i-1][j-1];
				}
				if(mtx[i-1][j] > 0){
					mtx[i][j] += mtx[i-1][j];
				}
				if(mtx[i-1][j+1] > 0){
					mtx[i][j] += mtx[i-1][j+1];
				}
			}
		}
	}
	mtx[x-1][b] = 0;
	mtx[x-1][b] += mtx[x-2][b-1] + mtx[x-2][b] + mtx[x-2][b+1];
	showMeTable(); //calls showMeTable() void. -- LANE #6
	
}
return 0;
}
