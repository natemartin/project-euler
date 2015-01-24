int main() {
  int i,j,k;
  long long int dec[102][10];
  long long int inc[102][10];

  for(i = 0; i < 10; i++)
    dec[1][i] = inc[1][i] = 1;
  for(i = 2; i < 102; i++) {
    for(j = 1; j < 10; j++) {
      long long int total = 0;
      for( k = j; k > 0; k--) {
        total += dec[i-1][k];
      }
      dec[i][j] = total + 1;
      printf("%llu %llu %llu\n", i, j, dec[i][j]);
    }
  }
  for(i = 2; i < 102; i++) {
    for(j = 1; j < 10; j++) {
      long long int total = 0;
      for( k = j; k < 10; k++) {
        total += inc[i-1][k];
      }
      inc[i][j] = total;
      printf("%llu %llu %llu\n", i, j, inc[i][j]);
    }
  }
  long long int total = 0;
  for(i = 1; i < 101; i++)
    for(j = 1; j < 10; j++)
      total+= (dec[i][j]+inc[i][j]);
  printf("%llu\n", total - 9*100);
}
