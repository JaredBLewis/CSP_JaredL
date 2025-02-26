// Jared Lewis, Old Enough C
#include <stdio.h>
#include <string.h>
//to vote: 18
//to drive: 16
//to get learner's permit: 15
//to go to school: 5
int age;

int main(void){
    printf("\n");
    printf("Hello, and welcome to my program!\n");
    printf("This program will determeine what you are old enough to do.\n");

    printf("How old are you?: \n");
    scanf("%d", &age);

    if(age >= 18){
        printf("You are old enough to vote.\n");
    }else if(age >= 16){
        printf("You are old enough to drive.\n");
    }else if(age >= 15){
        printf("You are old enough to get a learner's permit.\n");
    }else if(age >= 5){
        printf("You are old enough to go to school.\n");
    }else{
        printf("You are really young...\n");
    }


    return 0;
}