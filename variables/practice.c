#include <stdio.h>

int small_number = 9;
int large_number = 117;

int main(void) {
    char name;
    printf("what is your name?: \n");
    scanf("%a", &name);

    char breakfast;
    printf("What did you have for breakfast?: \n");
    scanf("%c", &breakfast);

    char fav_color;
    printf("What is your favorite color?: \n");
    scanf("%d", &fav_color);

    char school;
    printf("What School do you attend?: \n");
    scanf("%e", &school);

    int year;
    printf("What year is it?: \n");
    scanf("%f", &year);

    char eye_color;
    printf("What color are your eyes?: \n");
    scanf("%g", &eye_color);

    int age;
    printf("How old are you?: \n");
    scanf("%i", &age);

    char fav_subject;
    printf("What is your favorite subject in school?: \n\n");
    scanf("%n", &fav_subject);

    printf("Hello %a, I understand that you are %i years old, and have %g eyes. \n", name, age, eye_color) ;
    printf("You attend school at %e, in the year %f, and you ate %c for breakfast today. \n", school, year, breakfast);
    printf("Your favorite color is %d and your favorite subject in school is %n.", fav_color, fav_subject);
    return 0;
}