#include <stdio.h>
#include <iostream>
#include <algorithm>

#define BUF 100

int main(void){
    int N;
    int L[BUF];
    
    //input
    std::cin >> N;
    for(int i=0;i<N;i++) std::cin >> L[i];

    //output
    std::cout << N;
    for(int i=0;i<N;i++) std::cout << L[i];
    
    int total_size=0;
    for(int i=0;i<N;i++) total_size = total_size + L[i];

    std::cout << total_size;
    sort(L,L+N,std::greater<int>());
    for(int i=0;i<N;i++) std::cout << L[i] << "\r\n";


    int total=0;
    for(int i=0;i<N-1;i++){
        total = total + L[N-i-1]+L[N-i-2];
        L[N-i-2]=L[N-i-1]+L[N-i-2];
        L[N-i-1]=0;
    }
    std::cout << total;
}
