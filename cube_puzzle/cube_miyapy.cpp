#include <stdio.h>
#include <string>
#include <iostream>

#define CHAR_BUFFER 1000
#define STR_BUFFER 1000

int main(void){

    int N; //parts number
    int M; //length of cube
    std::string str[STR_BUFFER];
        //input file
    printf("parts number N:\r\n");
    scanf("%d",&N);
    printf("parts number M:\r\n");
    scanf("%d",&M);
    std::getline(std::cin,str[0]);

    for(int i=0;i<N;i++){
        std::getline(std::cin,str[i]);
    }

    //test out
    printf("N:%d,M:%d\r\n",N,M);
    for(int i=0;i<N;i++){
        std::cout <<  str[i]<<"\r\n";
    }
    int parts[100][100][3]

}

