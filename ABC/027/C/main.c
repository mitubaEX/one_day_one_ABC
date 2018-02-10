#include<stdio.h>

// 3 -> 右，左
// 4 -> 左，右

int main(void){
  long long num;
  int depth = 0;
  long long x = 1;
  scanf("%lld", &num);
  for(long long n = num; n > 0; n /= 2)
    depth++;
  // printf("%d\n", depth);
  if(depth % 2 == 0){
    int turn = 0;
    while(1){
      if(turn == 0){
        x = x * 2;
        if(x > num){
          printf("Aoki\n");
          break;
        }
        turn++;
      } else {
        x = x * 2 + 1;
        if(x > num){
          printf("Takahashi\n");
          break;
        }
        turn--;
      }
    }
  } else {
    int turn = 0;
    while(1){
      if(turn == 0){
        x = x * 2 + 1;
        if(x > num){
          printf("Aoki\n");
          break;
        }
        turn++;
      } else {
        x = x * 2;
        if(x > num){
          printf("Takahashi\n");
          break;
        }
        turn--;
      }
    }
  }
}
