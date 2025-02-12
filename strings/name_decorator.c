// Jared Lewis, Name Decorator C
#include <stdio.h>
#include <string.h>

int main(void){
    printf("\n");
    printf("Hello and welcome to name decorator!\n");

    char name[20];
    printf("What is your first name?:");
    scanf("%s", name);

    char left[50] = "#(///";
    char right[10] = "///)#";
    strcat(left, name);
    strcat(left, right);

    printf("3\n\n");
    printf("2\n\n");
    printf("1\n\n");

    printf("Your decorated name is %s\n", left);

    return 0;
}