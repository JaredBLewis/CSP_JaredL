// Jared Lewis, Time of Day C
#include <stdio.h>
#include <time.h>

int main(void){
    printf("\n");
    printf("Hello, and welcome to my program!\n");
    char name[20];
    printf("What is your name?: ");
    scanf("%s", name);

    time_t rawtime;
    struct tm * timeinfo;
    timeinfo = localtime(&rawtime);
    time_t now = time(NULL);
    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    printf("%d\n", hour);
    return 0;
}