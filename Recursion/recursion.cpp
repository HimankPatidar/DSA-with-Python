#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <bitset>
#include <iterator>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <cassert>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
using namespace std;

int sum(int n){

    if(n==0) return 0;
    return n+sum(n-1);
}

int fib(int n){
    if (n<=1) return n;

    return fib(n-1)+fib(n-2);
}

void printf(int ind, vector<int> &ds, int arr[], int n){
    if (ind ==n){
        for (auto it : ds){
            cout<<it<<" ";
        }
        cout<<endl;
        return;
    }

    // take or pick the particular index into the subsequence 
    ds.push_back(arr[ind]);
    printf(ind+1, ds, arr, n);
    ds.pop_back();

    // not take or not pick the particular index into the subsequence
    printf(ind+1, ds, arr, n);
}




// int main(){
//     int arr[] = {3,1,2};
//     int n = 3;
//     // cout << "Enter a number: ";
//     // cin >> n;
//     vector<int>ds;
//     printf(0 ,ds, arr, n);

//     // cout << sum(n) << endl;
//     cout << fib(n) << endl;


//     return 0;
// }


int main(){
    string s;
    cin>>s;

    int hash[26] = {0};
    for(int i=0; i<s.size(); i++){
        hash[s[i]-'a']++;
    }
    int q;
    cin>>q;
    while(q--){
        int n;
        cin>>n;
        int cnt = 0;
        for(int i=0; i<26; i++){
            if(hash[i]>n){
                cnt += hash[i]-n;
            }
        }
        cout<<cnt<<endl;
    }
}