#include <stdio.h>


int main(void){
    int c500,c100,c50,c10,c5,c1;
    int A;
    int p500,p100,p50,p10,p5,p1;
    int max_coin;
    
    //input
    printf("input c500\r\n");
    scanf("%d",&c500);
    printf("input c100\r\n");
    scanf("%d",&c100);
    printf("input c50\r\n");
    scanf("%d",&c50);
    printf("input c10\r\n");
    scanf("%d",&c10);
    printf("input c5\r\n");
    scanf("%d",&c5);
    printf("input c1\r\n");
    scanf("%d",&c1);
    printf("input A\r\n ");
    scanf("%d",&A);


    //500
    max_coin= A/500;
    p500 = max_coin;
    if(max_coin>c500) p500=c500;
    A = A-500*p500;

    //100
    max_coin= A/100;
    p100 = max_coin;
    if(max_coin>100) p100=c100;
    A = A-100*p100;

    //50
    max_coin= A/50;
    p50 = max_coin;
    if(max_coin>c50) p50=c50;
    A = A-50*p50;

    //10
    max_coin= A/10;
    p10 = max_coin;
    if(max_coin>c10) p10=c10;
    A = A-10*p10;

    //1

    max_coin= A;
    p1 = max_coin;
    if(max_coin>c1) printf("cannnot pay");
    else{
        printf("500:%d,100:%d, 50:%d, 10:%d,5:%d 1:%d, ",p500,p100,p50,p10,p5,p1);
    }
}
