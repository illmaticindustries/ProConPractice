#include <stdio.h>
#include <math.h>

#define BUF 1000

int main(void){
    int  n;
    int  r;
    int X[BUF];
   
    //input
    printf("input n\r\n");
    scanf("%d",&n);
    printf("input r\r\n");
    scanf("%d",&r);
    printf("input X\r\n");
    for(int i=0;i<n;i++){
        scanf("%d\r\n",X+i);
    }

    //out put
    
    printf("%d,%d\r\n",n,r);
    for(int i=0;i<n;i++){
        printf("%d\r\n",X[i]);
    }
   
    //label
    int l[BUF];
    for(int i=0;i<n;i++) l[i]=0; //initialize label
 
 
    int k;
    int start_no = 0;
    while(1){
       for(int i = 0;i<n;i++){
            if(X[i]<=X[start_no]+10){
                k=i;
                //printf("k:%d\r\n",k);
            } 
        }

       l[k]=1;
       if(k==n-1)break;
        for(int i= 0;i<n;i++){
            if(X[i]<=X[k]+10){
                start_no = i;
            }   
        }
        if(start_no == n-1)break;
        start_no++;
    }

    int sum=0;
    for(int i=0;i<n;i++)sum = sum+l[i];
    printf("answ:%d\r\n",sum);

}



