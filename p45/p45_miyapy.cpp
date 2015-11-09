#include <stdio.h>
#include <math.h>

#define BUF 100

int main(void){
    int  n;
    char S[BUF];
    char T[BUF];
    
    //input
    printf("input n\r\n");
    scanf("%d",&n);
    printf("input s\r\n");
    scanf("%s",S);

    printf("%s\r\n",S);
    
    int start=0;
    int i=0;
    
    for(i=0;i<n;i++){
        if(S[start]<S[start+n-i-1]){
            T[i]=S[start];
            start++;
            printf("%c\r\n",T[i]);
        }else{
            T[i]=S[start+n-i-1];
            printf("%c\r\n",T[i]);
        }
    }
    printf("answ:%s",T);

}



