// Jared Lewis, Silly Senetences C
#include <stdio.h>


int main(void){
    printf("Hello, and welcome to Silly sentance Creator!\n");

    char color[20];
    printf("Please enter a single color: ");
    scanf("%s", color);

    char name[20];
    printf("Please enter a male name: ");
    scanf("%s", name);

    char vehicle[20];
    printf("Please enter a single type of vehicle: ");
    scanf("%s", vehicle);

    char animal[20];
    printf("Please enter an animal: ");
    scanf("%s", animal);

    char famous_person[20];
    printf("Please enter the first name of a famous person: ");
    scanf("%s", famous_person);

    printf("It was a %s day when %s decided to take a ride in his %s when he saw a %s chasing %s down the street. \n", color, name, vehicle, animal, famous_person);
    
    return 0;
}