#include<stdio.h>
#include<conio.h>
int main(){
    float a[5]={0.5,0.2,0.9,0.1,0.7},t;
    int i,j;

    for(i=0;i<4;i++)
     for(j=0;j<4-i;j++)
      if(a[j]>a[j+1]){
        t=a[j]; a[j]=a[j+1]; a[j+1]=t;
      }

    for(i=0;i<5;i++) printf("%.1f ",a[i]);
}