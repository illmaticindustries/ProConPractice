#include <stdio.h>
#include <math.h>

#define BUF 100

int main(void){
    int  n;
    char S[BUF];
    char T[BUF]="";
    
    //input
    printf("input n\r\n");
    scanf("%d",&n);
    printf("input s\r\n");
    scanf("%s",S);

    //out put
    
    printf("%d,%s\r\n",n,S);
    
    //start computation
    int start=0;
    int i=0;
    

    for(i=0;i<n;i++){
        if(S[start]<S[start+n-i-1]){
            T[i]=S[start];
            start++;
            //printf("%c\r\n",T[i]);
        }else if(S[start]>S[start+n-i-1]){
            T[i]=S[start+n-i-1];
            //printf("%c\r\n",T[i]);
        }else{
            //printf("equal");
            int j=0;
                       
            while(S[start+j]==S[start+n-i-1-j]){
                j++; 
                if(j>n-start-1)break;    
            }
            //printf("%di.%d,%d",j,start+j,start+n-i-j-1);
            if(S[start+j]<S[start+n-i-1-j]){ 
                T[i]=S[start];
                start++;
                //printf("%c\r\n",T[i]);
       
            }else{
                T[i]=S[start+n-i-1];
                //printf("%c\r\n",T[i]);
            }
        }
    }
    printf("answ:%s\r\n",T);

}



