//Jared Lewis, C Practice
#include <stdio.h>

int small_number = 9;
int large_number = 117;

int main(void) {
    char name[20];
    printf("what is your name?: \n");
    scanf("%s", name);
    
    char breakfast[20];
    printf("What did you have for breakfast?: \n");
    scanf("%s", breakfast);

    char fav_color[20];
    printf("What is your favorite color?: \n");
    scanf("%s", fav_color);

    char school[20];
    printf("What School do you attend?: \n");
    scanf("%s", school);

    int year;
    printf("What year is it?: \n");
    scanf("%d", &year);

    char eye_color[20];
    printf("What color are your eyes?: \n");
    scanf("%s", eye_color);

    int age;
    printf("How old are you?: \n");
    scanf("%d", &age);

    char fav_subject[20];
    printf("What is your favorite subject in school?: \n");
    scanf("%s", fav_subject);

    printf("Hello %s, I understand that you are %d years old, and have %s eyes. \n", name, age, eye_color);
    printf("You attend school at %s, in the year %d, and you ate %s for breakfast today. \n", school, year, breakfast);
    printf("Your favorite color is %s and your favorite subject in school is %s.", fav_color, fav_subject);
    return 0;
}