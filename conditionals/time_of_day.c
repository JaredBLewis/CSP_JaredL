// Jared Lewis, Time of Day C
#include <stdio.h>
#include <time.h>

int main(void){
    printf("\n");
    printf("Hello, and welcome to my program!\n");
    char name[20];
    printf("What is your name?: ");
    scanf("%s", name);

   time_t seconds;
   seconds = time(NULL);
   time_t rawtime;
   struct tm * timeinfo;
   time(&rawtime);
   timeinfo = localtime(&rawtime);
   printf("Current time & date is %s", asctime(timeinfo));
   time_t now = time(NULL);
   struct tm * tm_struct = localtime(&now);
   int hour = tm_struct->tm_hour;

    if(hour < 12){
        printf("Good morning, %s!\n", name);
    } else if(hour < 18){
        printf("Good afternoon, %s!\n", name);
    } else {
        printf("Good evening, %s!\n", name);
    }
    return 0;
}