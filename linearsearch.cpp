#include <iostream>
using namespace std;
int main() {

    int target;
    int arr[100];
    int i;
    int flag=0;
    cin>>target;
    cout<<"please enter the array and the target to find the target"<<endl;
    for(i=0;i<5;i++) {
        cin>>arr[i];
      if(arr[i]==target){
        flag=1;
      }
    }
    if(flag==1) {
            cout<<"target is found"<<endl;
    } else{
            cout<<"target is not found"<<endl;
     }
} 
