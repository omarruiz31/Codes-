#include <stdio.h>
int main(){
  printf("Elige una tabla de multiplicar\n");
  int tabla;
  scanf("%d",&tabla);
   for (int i=10;i<=1;i--){
    printf("%d\n",tabla*i);
   }
}