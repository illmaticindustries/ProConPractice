#include <stdio.h>
#include <math.h>

#define BUF  100000

int nearest_job(int now, int *s,int *t,int n);

int main(void){
    int  n;
    int s[BUF];
    int t[BUF];
    
    //input
    printf("input n\r\n");
    scanf("%d",&n);
    printf("input s\r\n");
    for(int i=0;i<n;i++)scanf("%d",s+i);
    
    //out put 
    printf("input t\r\n");
    for(int i=0;i<n;i++)scanf("%d",t+i);
    printf("%d\r\n",n);
    for(int i=0;i<n;i++) printf("%d\r\n",s[i]);
    for(int i=0;i<n;i++) printf("%d\r\n",t[i]);
    
    //compute
    int now = 0;
    int count = 0;
    int ter = 0;    
    int flag = 0;
    for(int i = 0;i<n;i++){
        ter =  nearest_job(now,s,t,n);
        if(ter == -1){}
        else{
            count++;        
            now = t[ter];
            t[ter]=1000000000;
        };
    }
    printf("%d",count);
}

int nearest_job(int now,int *s,int *t,int n){
    int min = 1000000000;
    int index = n;
    for(int i=0;i<n;i++){
        if((s[i]>now)&&(t[i]<min)){
            min = t[i];
            index = i;
        }
    }
    if(min == 1000000000) index = -1;
    printf("%d",index);
    return index;

}

