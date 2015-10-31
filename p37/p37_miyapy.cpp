#include <stdio.h>
#include <queue>
using namespace std;

#define BUF_SIZE 10000
void print_maze(int n,int m, char *maze);

int n;
int m;

struct pos{
    int x;
    int y;
};

int main(void){
   char maze[BUF_SIZE];
    //input
    printf("input n\r\n");
    scanf("%d",&n);
    printf("input m\r\n");
    scanf("%d",&m);
    printf("input maze\r\n");
    for(int i=0;i<n;i++){
        scanf("%s",maze+i*m);
    }
    print_maze(n,m,maze);


    int Sx,Sy;//start
    //search start
    for(int i=0;i<n*m;i++){
        if(maze[i]=='S'){
            Sx = i%m;
            Sy = i/m;
        }
    }

    struct pos G;
    //search goal 
    for(int i=0;i<n*m;i++){
        if(maze[i]=='G'){
            G.x = i%m;
            G.y = i/m;
        }
    }

    queue<struct pos> q1;
    struct pos a;
    a.x = Sx;a.y=Sy;
    q1.push(a); //set start position 
    
    int count = 0;
    int num = 0;//size of packman
    int flag = 1;//loop flag
    while(flag){
        num = q1.size();
        for(int i=0;i<num;i++){
            struct pos p = q1.front();
            if((p.x==G.x)&&(p.y==G.y)){
                printf("%d\r\n",count);
                flag = 0;//down flag
                break;
            }
            maze[p.y*m+p.x]='#';
            //check up
            if((p.y>0)&&(maze[p.y*m+p.x-m]!='#')){
                struct pos a;
                a.x = p.x;
                a.y= p.y-1;
                q1.push(a);
            }
            //check left
            if((p.x>0)&&(maze[p.y*m+p.x-1]!='#')){
                struct pos a;
                a.x = p.x-1;
                a.y= p.y;
                q1.push(a);
            }
            //check right
            if((p.x<m)&&(maze[p.y*m+p.x+1]!='#')){
                struct pos a;
                a.x = p.x+1;
                a.y= p.y;
                q1.push(a);
            }
            //check down
            if((p.y<n)&&(maze[p.y*m+p.x+m]!='#')){
                struct pos a;
                a.x = p.x;
                a.y= p.y+1;
                q1.push(a);
            }
            q1.pop();
        }
        count++;
    }

}

void print_maze(int n,int m,char *maze){
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            printf("%c",maze[m*i+j]);
        }
        printf("\r\n");
    }
}
