#include <iostream>
using namespace std;

int binarysearch(int arr[],int l,int r, int x) {
     while(l<=r){
        int m = l+(r-l)/2; 

    if(arr[m]==x) {
        cout<<"Element found m"<<endl;
    }
    if(arr[m]<x) {
        l=m+1;
    } else{
        l=m-1;
    }
    return -1;
    
    }

}

int main(void) {

     int arr[]={2,3,4,5,6};
     int x = 10;
     int n = sizeof(arr) / sizeof(arr[0]); 
     int result = binarysearch(arr, 0, n - 1, x);
      (result == -1)
        ? cout << "Element is not present in array"
        : cout << "Element is present at index " << result;
    return 0;
}


   
   
