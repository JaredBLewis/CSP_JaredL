// Jared Lewis, Name Decorater C
#include <stdio.h>
#include <string.h>

int main(void){
    printf("\n");
    printf("Hello and welcome to name decorator!\n");

    char name[50];
    printf("What is your first name?:");
    scanf("%s", name);

    char left[] = "#(///";
    char right[] = "///)#";
    strcat(left, name);
    strcat(left, right);

    printf("3\n\n");
    printf("2\n\n");
    printf("1\n\n");

    printf("Your decorated name is %s\n", left);

    return 0;
}