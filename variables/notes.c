// Jared Lewis, Variables Notes C
#include <stdio.h>

char name[20];
int age;
float pi;

int main(void){
    printf("Welcome, what is your name?: \n");
    scanf("%s", name);
    printf("How old are you?: \n");
    scanf("%d", &age);
    printf("Print out as much of pi as you know: \n");
    scanf("%f", &pi);
    printf("Hello %s! You are %d years old, and you like the number %f", name, age, pi);
    return 0;
}