#include<stdio.h>
int main(void){
  int x, k;
  scanf("%d %d", &x, &k);

  int tmp = 1;
  for(int i = 0; i < k; i++){
    tmp *= 10;
  }

  int y = tmp;
  while(1){
    if(x + 1 <= y){
      printf("%d\n", y);
      break;
    }
    y += tmp;
  }
}
